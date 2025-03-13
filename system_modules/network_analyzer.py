"""
Network Analysis Module (REAL - using subprocess and re)

This module provides functions to fetch network status data for CyberNexus.

It uses 'speedtest-cli' for speed tests and 'subprocess' with 'ip a'
to get internal IP addresses (avoids netifaces build issues on Windows).

Future enhancements:
- Implement more advanced network diagnostics.
- Integrate basic network security scanning capabilities.
"""

import subprocess
import requests
import speedtest
import re  # Import the regular expression module


def get_network_status():
    """Returns network status data, including speed test and IP addresses."""
    try:
        st_cli = speedtest.Speedtest()
        st_cli.download()
        st_cli.upload()
        download_speed = f"{st_cli.results.download / 1_000_000:.2f} Mbps"
        upload_speed = f"{st_cli.results.upload / 1_000_000:.2f} Mbps"
        ping = f"{int(st_cli.results.ping):.0f} ms"
    except speedtest.SpeedtestException as e:
        download_speed = "N/A (Speedtest Error)"
        upload_speed = "N/A (Speedtest Error)"
        ping = "N/A (Speedtest Error)"

    ip_addresses = {}
    try:
        # Execute 'ip a' command
        ip_a_output = subprocess.check_output(["ip", "a"], text=True)

        # Parse the output using regular expressions
        interface = None
        for line in ip_a_output.splitlines():
            line = line.strip()
            if line.endswith(":"):  # Line indicating interface name
                interface = line[:-1]  # Remove the ":"
                ip_addresses[interface] = "N/A"  # Initialize IP for this interface
            elif "inet " in line:  # Line containing IPv4 address
                match = re.search(r"inet (\d+\.\d+\.\d+\.\d+)", line)  # Regex to extract IPv4
                if match and interface:
                    ip_addresses[interface] = match.group(1)  # Extract the IP address

    except FileNotFoundError:  # 'ip' command not found
        ip_addresses["Error"] = "ip command not found"
    except subprocess.CalledProcessError as e:  # Error running 'ip a'
        ip_addresses["Error"] = f"Error running ip a: {e}"

    try:
        external_ip = requests.get('https://api.ipify.org').text
    except requests.exceptions.RequestException:
        external_ip = "N/A (External IP Error)"

    return {
        "download_speed": download_speed,
        "upload_speed": upload_speed,
        "ping": ping,
        "internal_ips": ip_addresses,
        "external_ip": external_ip,
    }


def format_network_status_response(net_stats):
    """Formats network status data into a user-friendly markdown response."""
    net_response = "<b>Network Status:</b>\n"
    net_response += f"- Download Speed: {net_stats['download_speed']}\n"
    net_response += f"- Upload Speed: {net_stats['upload_speed']}\n"
    net_response += f"- Ping: {net_stats['ping']}\n"
    net_response += "- Internal IPs:\n"
    for interface, ip in net_stats['internal_ips'].items():
        net_response += f"  - {interface}: {ip}\n"
    net_response += f"- External IP: {net_stats['external_ip']}\n"
    return net_response
