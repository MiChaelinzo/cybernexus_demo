import streamlit as st
import psutil
import speedtest
import netifaces
import requests
import yaml
import time
import random

# --- Realistic (Symbolic) Quantum Computing Imports ---
# These imports represent potential future quantum libraries that *could*
# be used in advanced network monitoring for enhanced performance and security.
try:
    from braket.circuits import Circuit, Qubit, FreeParameter, Observable # AWS Braket circuit elements (Symbolic)
    from braket.devices import LocalSimulator, AwsDevice # AWS Braket device interfaces (Symbolic)
    from qiskit import QuantumCircuit, transpile, Aer, assemble # IBM Qiskit circuit tools (Symbolic)
    HAS_QUANTUM_LIBS = True
except ImportError:
    HAS_QUANTUM_LIBS = False
    print("Info: Symbolic quantum SDKs (braket, qiskit) not fully installed. Running with classical simulations.")


st.set_page_config(
    page_title="CyberNexus Pi Eyes AI-Agent 🌌 (Quantum-VPC Edition)",
    page_icon="🛜",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Project Description - More Realistic Quantum Tone ---
st.markdown(
    """
    <style>
    body {
        color: #eee;
        background-color: #111;
    }
    .stApp {
        background-color: rgba(17, 17, 17, 0.85);
    }
    h1, h2, h3, h4, h5, h6 {
        color: #00ffff;
        font-family: 'Courier New', monospace;
    }
    .stButton>button {
        color: #00ff7f;
        background-color: #333;
        border-color: #00ff7f;
    }
    .stTextInput>div>div>input, .stNumberInput>div>div>input, .stTextArea>div>div>textarea {
        color: #00ff7f;
        background-color: #222;
        border: 1px solid #00ff7f;
    }
    .stSelectbox>div>div>div>div {
        color: #00ff7f;
        background-color: #333;
    }
    .css-1egvi7u { /* Streamlit main content */
        color: #00ff7f;
    }
    div.stButton > button:first-child {
        background-color: #007bff;
        color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("CyberNexus Pi Eyes AI-Agent 🌌 (Quantum-VPC Edition)")

st.markdown(
    """
    ## 🌐 Quantum-VPC Network Sentinel 🌐

    **CyberNexus Pi Eyes AI-Agent (Quantum-VPC Edition)** is designed to explore the future of network monitoring and security within **Quantum-VPC** architectures. This demo illustrates how an AI-Agent, drawing inspiration from **quantum computing paradigms**, could revolutionize network threat detection and performance optimization.

    **Potential Quantum-Enhanced Capabilities (Demo Focus):**

    *   **Quantum-Accelerated Network Analysis:** Simulates near real-time network insights through **conceptually quantum-accelerated algorithms**, envisioning future processing speeds.
    *   **Quantum-Enhanced Anomaly Detection:** Explores the potential of **quantum-inspired machine learning models** (symbolically represented by libraries like Cirq & Qiskit) for superior malware and anomaly detection accuracy.
    *   **Quantum-Resilient Cyber-Defense:** Demonstrates adaptive security responses based on advanced analytics, hinting at **quantum-level resilience** against sophisticated threats.
    *   **Pi-hole Integration with Quantum Optimization:**  Presents enhanced ad-blocking as potentially benefiting from **quantum-optimized filtering strategies** for maximized efficiency.
    *   **Quantum-Scalable Monitoring Architecture:**  Outlines a monitoring framework conceptually designed for the demands of large-scale, **quantum-centric network environments**.

    **Important Disclaimer:** This is a conceptual technology demonstration.  **No actual quantum computation is performed in this demo.**  The inclusion of quantum SDK imports (like Braket & Qiskit) and "Quantum-" prefixes are to illustrate potential future directions and are purely symbolic for this educational demonstration.  Real-world quantum computing for network security is still in early research phases.
    """ , unsafe_allow_html=True)


def get_network_stats():
    """
    Retrieves network statistics using classical methods.
    Envisions future integration with quantum sensors for enhanced data acquisition.
    """
    net_io = psutil.net_io_counters()
    return {
        "bytes_sent": net_io.bytes_sent,
        "bytes_recv": net_io.bytes_recv,
        "packets_sent": net_io.packets_sent,
        "packets_recv": net_io.packets_recv,
        "errin": net_io.errin,
        "errout": net_io.errout,
        "dropin": net_io.dropin,
        "dropout": net_io.dropout,
    }


def analyze_network_traffic(prev_stats, current_stats):
    """
    Analyzes network traffic for anomalies using classical thresholding.
    Future versions may incorporate quantum machine learning for pattern recognition.
    """
    if prev_stats:
        bytes_sent_diff = current_stats["bytes_sent"] - prev_stats["bytes_sent"]
        bytes_recv_diff = current_stats["bytes_recv"] - prev_stats["bytes_recv"]
        packet_sent_diff = current_stats["packets_sent"] - prev_stats["packets_sent"]
        packet_recv_diff = current_stats["packets_recv"] - prev_stats["packets_recv"]
        errin_diff = current_stats["errin"] - prev_stats["errin"]
        errout_diff = current_stats["errout"] - prev_stats["errout"]
        dropin_diff = current_stats["dropin"] - prev_stats["dropin"]
        dropout_diff = current_stats["dropout"] - prev_stats["dropout"]

        if bytes_sent_diff < 0 or bytes_recv_diff < 0:
            return "Negative traffic volume detected: Potential counter reset or system instability."

        if packet_sent_diff < 0 or packet_recv_diff < 0:
            return "Negative packet count: Possible counter reset or data inconsistency."

        if errin_diff > 1000 or errout_diff > 1000 or dropin_diff > 100 or dropout_diff > 100:
            return "Elevated network errors or packet drops: Indicating potential network issues."


        if bytes_sent_diff > 1000000 or bytes_recv_diff > 1000000: # Example threshold - adjust as needed
            return "Anomaly Alert: High traffic volume detected. Investigating potential security breach." # More realistic alert message

    return None


def get_network_interfaces():
    """
    Retrieves network interface list using standard OS calls.
    Envisions future quantum-secured interface enumeration for enhanced privacy.
    """
    interfaces = netifaces.interfaces()
    return interfaces


def get_interface_addresses(interface):
    """
    Retrieves IP addresses for a network interface using classical methods.
    Future Quantum-VPC may utilize quantum key distribution for address verification.
    """
    addresses = netifaces.ifaddresses(interface)
    ip_addresses = []
    if netifaces.AF_INET in addresses:
        for ip_info in addresses[netifaces.AF_INET]:
            ip_addresses.append(ip_info['addr'])
    return ip_addresses



def get_pihole_stats(api_url, api_token):
    """
    Retrieves Pi-hole statistics via classical HTTP requests.
    Quantum communication layers could enhance API security and speed in the future.
    """
    headers = {"Authorization": f"Token: {api_token}"}
    try:
        response = requests.get(api_url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching Pi-hole stats: {e}")
        return None


def display_pihole_stats(pihole_data):
    """
    Displays Pi-hole statistics using Streamlit's classical UI elements.
    Quantum displays might offer richer, multi-dimensional data visualization in future interfaces.
    """
    if pihole_data:
        with st.expander("Pi-hole Stats (Quantum-Optimized Filtering Simulation)"): # More descriptive expander label
            st.metric("Total Queries (Processed)", pihole_data.get("total_queries", "N/A"))
            st.metric("Queries Blocked (Ads Prevented)", pihole_data.get("ads_blocked_today", "N/A"))
            st.metric("Percentage Blocked (Block Ratio)", f"{pihole_data.get('ads_percentage_today', 'N/A')}%")
            st.metric("Domains Blocked (Filter List Size)", pihole_data.get("domains_being_blocked", "N/A"))
            st.metric("Clients Ever Seen (Client History)", pihole_data.get("clients_ever_seen", "N/A"))
            st.metric("Unique Clients Today (Active Devices)", pihole_data.get("unique_clients_today", "N/A"))
            st.metric("Queries Cached (Cache Efficiency)", pihole_data.get("queries_cached", "N/A"))
            st.metric("Queries Forwarded (External DNS Lookups)", pihole_data.get("queries_forwarded", "N/A"))
            st.metric("DNS Resolvers Used (Upstream Servers)", pihole_data.get("dns_servers", "N/A"))
            # st.json(pihole_data) # Optionally display full JSON for debugging


def run_speedtest():
    """
    Runs a network speed test using speedtest-cli (classical).
    Future Quantum-VPC could utilize quantum sensors for more accurate latency measurements.
    """
    st = speedtest.Speedtest()
    st.download()
    st.upload()
    results_dict = st.results.dict()
    return results_dict


def display_speedtest_results(results):
    """
    Displays speedtest results using Streamlit metrics (classical UI).
    Quantum interfaces may provide more intuitive and detailed performance dashboards.
    """
    if results:
        with st.expander("Speed Test Results (Simulating Quantum-Speed Metrics)"): # More descriptive expander
            st.metric("Download Speed (Mbps)", f"{results.get('download') / 1_000_000:.2f} Mbps")
            st.metric("Upload Speed (Mbps)", f"{results.get('upload') / 1_000_000:.2f} Mbps")
            st.metric("Ping (Latency in ms)", f"{results.get('ping'):.2f} ms")
            st.metric("Data Sent (MB)", f"{results.get('bytes_sent') / 1_000_000:.2f} MB")
            st.metric("Data Received (MB)", f"{results.get('bytes_received') / 1_000_000:.2f} MB")
            st.write("Raw Speedtest JSON Data (for advanced analysis):") # Added label for JSON data
            st.json(results)


def main():
    """Main function to run the CyberNexus Pi Eyes AI-Agent (Quantum-VPC Edition) - DEMO."""
    st.sidebar.header("CyberNexus Quantum Core 🌌")

    st.sidebar.markdown("### Quantum Matrix Status (Simulated)") # Clarified "Simulated"
    cpu_usage = random.randint(1, 100)
    st.sidebar.markdown(f"- Quantum Processing Load: {cpu_usage}% (Simulated)") # More realistic label
    total_ram = random.choice([16, 32, 64, 128, 256, 512, 1024])
    used_ram = random.randint(1, total_ram)
    st.sidebar.markdown(f"- Quantum Memory Allocation: {used_ram}GB / {total_ram}GB (Simulated)") # More realistic label
    network_status = random.choice(["Quantum-Linked Securely", "Network Offline", "Neural Network Active", "Quantum Entanglement Ready"]) # More realistic statuses
    st.sidebar.markdown(f"- Network State: {network_status} (Simulated)") # More realistic label
    agi_core = random.choice(["AI-Agent: Quantum-Optimized", "AI-Agent: Idle", "AI-Agent: Processing Data", "AI-Agent: Overclocked"]) # More realistic statuses
    st.sidebar.markdown(f"- AI-Agent Core: {agi_core} (Simulated)") # More realistic label

    st.header("CyberNexus Pi Eyes AI-Agent 🌌 (Quantum-VPC Edition) - Network Monitoring Dashboard (Demo)") # Added "(Demo)" to header

    config_file = "cybernexus_config.yaml"
    try:
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        st.error(f"Configuration file '{config_file}' not found. Please create it as per documentation.") # Improved error message
        return
    except yaml.YAMLError as e:
        st.error(f"Error parsing configuration file '{config_file}': {e}. Check YAML syntax.") # Improved error message
        return

    pihole_api_url = config.get("pihole_api_url")
    pihole_api_token = config.get("pihole_api_token")

    if not pihole_api_url or not pihole_api_token:
        st.warning("Pi-hole API access is not configured in `cybernexus_config.yaml`. Pi-hole statistics are disabled.") # More informative warning
        pihole_enabled = False
    else:
        pihole_enabled = True

    placeholder = st.empty() # Placeholder for status messages
    interface_list = get_network_interfaces()
    selected_interface = st.selectbox("Select Network Interface for Monitoring (Quantum-Interface Select)", interface_list) # More descriptive label

    col1, col2 = st.columns(2) # Create two columns layout

    with col1: # Column for Network Stats and Analysis
        st.subheader("Real-time Network Statistics (Quantum-Enhanced View)") # More engaging subheader
        if selected_interface:
            st.write(f"Interface being monitored: **{selected_interface}** (Quantum-Focused Monitoring)") # More descriptive message
            interface_ips = get_interface_addresses(selected_interface)
            if interface_ips:
                st.write("Detected IP Addresses (Quantum-Identified):") # More descriptive label
                for ip in interface_ips:
                    st.code(ip)
            else:
                st.warning("No IP addresses detected on this interface (Quantum-Empty Subnet?).") # More evocative warning
        else:
            st.warning("Please select a network interface to begin monitoring (Quantum-Interface Required).") # More instructive warning

        if st.checkbox("Show Raw Interface Data (Quantum-Telemetry Stream)", False): # More evocative checkbox label
            if selected_interface:
                interface_addresses = netifaces.ifaddresses(selected_interface)
                st.json(interface_addresses) # Display raw data as JSON
            else:
                 st.warning("Select a network interface to view raw interface data.") # More specific warning

        if st.checkbox("Activate Quantum Network Anomaly Analysis", False): # More engaging checkbox label
            status_area = st.empty()
            placeholder.info("Quantum Network Anomaly Analysis is now active (Conceptual Simulation).") # More informative message

            prev_net_stats = get_network_stats() # Get initial stats

            while True: # Run analysis continuously
                current_net_stats = get_network_stats()
                anomaly = analyze_network_traffic(prev_net_stats, current_net_stats)
                if anomaly:
                    status_area.error(f"🚨 Quantum Anomaly Detected: {anomaly} 🚨 - Potential Threat Level: Elevated") # More dramatic alert
                else:
                    status_area.success("Quantum Network Status: Secure and Stable ✅ - No Anomalies Detected") # More reassuring status

                stats_df = pd.DataFrame([current_net_stats])
                st.dataframe(stats_df, use_container_width=True) # Display current stats

                prev_net_stats = current_net_stats # Update previous stats for next iteration
                time.sleep(config.get("monitoring_interval", 2)) # Use interval from config or default to 2 seconds

    with col2: # Column for Pi-hole and Speedtest
        st.subheader("Quantum Pi-hole Integration (Ad-Blocking)") # More descriptive header
        if pihole_enabled:
            if st.button("Retrieve Quantum Pi-hole Statistics"): # More action-oriented button label
                with st.spinner("Fetching Quantum Pi-hole data... (Quantum API Access)"): # More evocative spinner message
                    pihole_data = get_pihole_stats(pihole_api_url, pihole_api_token)
                    display_pihole_stats(pihole_data)
        else:
            st.info("Pi-hole integration is currently offline. Configure API access in `cybernexus_config.yaml`.") # More helpful info message

        st.subheader("Quantum Speed Test (Performance Diagnostics)") # More descriptive header
        if st.button("Initiate Quantum Speed Test"): # More action-oriented button label
            with st.spinner("Running Quantum Speed Diagnostics... (Quantum Measurement Underway)"): # More evocative spinner
                speedtest_results = run_speedtest()
                display_speedtest_results(speedtest_results)


    st.sidebar.markdown("---")
    st.sidebar.markdown(
        """
        <small>
        CyberNexus Pi Eyes AI-Agent (Quantum-VPC Edition) - Conceptual Demo<br/>
        For demonstration purposes only. Not for production use.<br/>
        Powered by Streamlit & Classical Computing Infrastructure<br/>
        Quantum-Inspired Concepts & Future-Forward Vision 🌌
        </small>
        """,
        unsafe_allow_html=True,
    )

if __name__ == "__main__":
    main()
