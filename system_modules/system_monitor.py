"""
System Monitoring Module (REAL)

This module provides functions to fetch Raspberry Pi system monitoring data.

It utilizes the 'psutil' library to get real-time system metrics.

Future enhancements:
- Add process monitoring and management capabilities.
- Implement logging and alerting for system anomalies.
"""

import psutil

def get_pi_status():
    """Returns Raspberry Pi system status data using psutil."""
    cpu_percent = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    disk = psutil.disk_usage('/')
    disk_percent = disk.percent
    temp = psutil.sensors_temperatures()
    cpu_temp = None
    if 'cpu_thermal' in temp: # or 'cpu-thermal' or similar, check your sensors_temperatures output
        cpu_temp_celsius = temp['cpu_thermal'][0].current
        cpu_temp = f"{cpu_temp_celsius:.1f}°C" # Format to one decimal place
    elif 'cpu-thermal' in temp: #Another common sensor name
        cpu_temp_celsius = temp['cpu-thermal'][0].current
        cpu_temp = f"{cpu_temp_celsius:.1f}°C"
    else:
        cpu_temp = "N/A" # Handle cases where sensor is not found

    return {
        "cpu_usage": f"{cpu_percent}%",
        "ram_usage": f"{memory_percent}%",
        "disk_usage": f"{disk_percent}%",
        "cpu_temperature": cpu_temp
    }

def format_pi_status_response(pi_stats):
    """Formats Pi-hole status data into a user-friendly markdown response."""
    status_response = "<b>Raspberry Pi System Status:</b>\n" # More formal title
    status_response += f"- **CPU Usage:** {pi_stats['cpu_usage']}\n" # Enhanced labels
    status_response += f"- **RAM Usage:** {pi_stats['ram_usage']}\n"
    status_response += f"- **Disk Usage:** {pi_stats['disk_usage']}\n"
    status_response += f"- **CPU Temperature:** {pi_stats['cpu_temperature']}\n"
    return status_response
