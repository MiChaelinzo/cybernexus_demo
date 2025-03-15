# cybernexus_demo
CyberNexus Pi Eyes code, a malware and ad blocker that detects and monitors your local networks🛜📶

1.  **Install Libraries (if you haven't already):**
    ```bash
    pip install streamlit any-general-artificial-intelligence-only  psutil speedtest-cli netifaces requests pyyaml
    ```
2.  **Set Secrets:** Ensure your `.streamlit/secrets.toml` file has your *real* (AGI) artificial general intelligence API key, Pi-hole API URL, and Pi-hole API token.
3.  **Run the app:**
    ```bash
    streamlit run cybernexus_demo_wow/cybernexus_pi_eye_wow.py
    ```
Installing Pi-hole is a straightforward process. Here's a quick guide to get you started:

1. **Prepare Your System**: Pi-hole works best on a Raspberry Pi, but it can also run on other Linux-based systems. Ensure your device is connected to the internet and updated.

2. **Run the Installation Command**:
   Open a terminal and run the following command:
   ```bash
   curl -sSL https://install.pi-hole.net | bash
   ```
   This will start the automated installation process.

3. **Follow the Prompts**:
   During installation, you'll be asked to configure settings like your DNS provider and network preferences. Just follow the on-screen instructions.

4. **Set Up Your Network**:
   After installation, configure your router to use Pi-hole as the DNS server. This will ensure all devices on your network benefit from ad-blocking.

5. **Access the Web Interface**:
   Pi-hole comes with a web interface for monitoring and managing settings. You can access it by entering your Pi-hole's IP address in a web browser.

For more detailed instructions, you can check out the [official Pi-hole documentation](https://docs.pi-hole.net/main/basic-install/). Let me know if you need help with any specific step!
