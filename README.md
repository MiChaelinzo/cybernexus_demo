# cybernexus_demo
CyberNexus Pi Eyes AI-Agent demo code, an anti-virus, malware, and ad blocker, etc. that detects and monitors your local networks🛜📶
Can be installed in a Quantum-PC for more processors and speed, etc.

1.  **Install Libraries (if you haven't already):**
    ```bash
    pip install streamlit any-general-artificial-intelligence-only  psutil speedtest-cli netifaces requests pyyaml
    ```
2.  **Set Secrets:** Ensure your `.streamlit/secrets.toml` file has your *real* (AGI) artificial general intelligence API key, Pi-hole API URL, and Pi-hole API token.
3.  **Run the app:**
    ```bash
    streamlit run cybernexus_demo_wow/cybernexus_pi_eye_wow.py
    ```
Installing Pi-hole 🌌  is a straightforward process. Here's a quick guide to get you started:

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

To run and install CyberNexus Pi-Eye Q AI-powered agent for network security in a quantum enviroment or system for testing:

Running a Quantum Virtual Private Cloud (VPC) on cloud platforms like AWS, Google Cloud, IBM Cloud, or Microsoft Azure involves setting up a quantum computing environment within a virtual network. Below are general instructions for setting up a quantum VPC on each platform, including terminal access.

<img width="937" alt="Screenshot 2025-03-28 121639" src="https://github.com/user-attachments/assets/319a2981-0262-4358-aa64-7e1c01c2a544" />

<img width="932" alt="Screenshot 2025-03-17 150308" src="https://github.com/user-attachments/assets/422948db-f1d4-4350-a5b4-6ff031fd7fc2" />

![485310300_690097120029453_6660953306619613434_n](https://github.com/user-attachments/assets/8cad3c8f-0715-4d2e-bd14-3dd1726adee7)

<img width="929" alt="Screenshot 2025-03-28 121747" src="https://github.com/user-attachments/assets/4cccb710-3500-4f52-b1a6-a4ba18b1469e" />

---

### **1. AWS (Amazon Web Services)**
AWS offers quantum computing services through **Amazon Braket**.

#### Steps:
1. **Create a VPC**:
   - Go to the AWS Management Console.
   - Navigate to **VPC > Create VPC**.
   - Define the IP range, subnets, and security groups.

2. **Set Up Amazon Braket**:
   - Go to the **Amazon Braket** console.
   - Create a quantum task or notebook instance.
   - Attach the notebook instance to your VPC for secure access.

3. **Access via Terminal**:
   - Launch an EC2 instance within the VPC.
   - SSH into the EC2 instance using:
     ```bash
     ssh -i your-key.pem ec2-user@your-ec2-ip
     ```
   - Install the Amazon Braket SDK:
     ```bash
     pip install amazon-braket-sdk
     ```
   - Run quantum circuits using the Braket SDK.

---

### **2. Google Cloud**
Google Cloud provides quantum computing through **Cirq** and **Quantum Engine**.

#### Steps:
1. **Create a VPC**:
   - Go to the Google Cloud Console.
   - Navigate to **VPC Network > Create VPC**.
   - Define subnets and firewall rules.

2. **Set Up Quantum Engine**:
   - Enable the **Quantum Engine API** in the Google Cloud Console.
   - Create a quantum processor or simulator.

3. **Access via Terminal**:
   - Launch a Compute Engine VM within the VPC.
   - SSH into the VM:
     ```bash
     gcloud compute ssh your-vm-name --zone=your-zone
     ```
   - Install Cirq:
     ```bash
     pip install cirq
     ```
   - Use Cirq to write and run quantum circuits.

---

### **3. IBM Cloud**
IBM Cloud offers quantum computing via **IBM Quantum Experience**.

#### Steps:
1. **Create a VPC**:
   - Go to the IBM Cloud Console.
   - Navigate to **VPC > Create VPC**.
   - Define subnets and security groups.

2. **Set Up IBM Quantum**:
   - Go to the **IBM Quantum Experience** dashboard.
   - Generate an API token for programmatic access.

3. **Access via Terminal**:
   - Launch a Virtual Server Instance within the VPC.
   - SSH into the instance:
     ```bash
     ssh root@your-instance-ip
     ```
   - Install the Qiskit SDK:
     ```bash
     pip install qiskit
     ```
   - Use Qiskit to run quantum circuits on IBM Quantum backends.

---

### **4. Microsoft Azure**
Azure provides quantum computing through **Azure Quantum**.

#### Steps:
1. **Create a VPC (Virtual Network)**:
   - Go to the Azure Portal.
   - Navigate to **Virtual Networks > Create Virtual Network**.
   - Define subnets and network security groups.

2. **Set Up Azure Quantum**:
   - Go to the **Azure Quantum** workspace.
   - Create a quantum workspace and link it to your virtual network.

3. **Access via Terminal**:
   - Launch a Virtual Machine within the Virtual Network.
   - SSH into the VM:
     ```bash
     ssh your-user@your-vm-ip
     ```
   - Install the Azure Quantum SDK:
     ```bash
     pip install azure-quantum
     ```
   - Use the SDK to submit quantum jobs.

