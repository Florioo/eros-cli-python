[![Python test package installation](https://github.com/Florioo/eros-python-logger-app/actions/workflows/test_installation.yml/badge.svg)](https://github.com/Florioo/eros-python-logger-app/actions/workflows/test_installation.yml)

# Eros Communication Logger

This Python program is built on top of the Eros library to facilitate the easy logging of communications through various transport protocols including UART, UDP, and TCP. By specifying the desired parameters such as port, baud rate, vendor ID for UART, and IP address for UDP and TCP, users can monitor the data flow and analyze communication patterns in a simple and efficient manner.

## Requirements

This program requires the following Python packages:
- eros-core
- click
- 
## Installation using pip

Follow the steps below to install Eros-View:

### Step 1: Install the Package with PIP

Install the package using pip. Run the command:

```
pip install git+https://github.com/Florioo/eros-python-logger-app
```

### Step 2: Verify Installation

After installation, you can verify if Eros-View was installed correctly. Run the command:
```
eros-view --help
```
If the installation was successful, this command should show the help menu of Eros-View.


## Installation from source

Follow the steps below to install Eros-View:

### Step 1: Clone the Repository

Clone the repository to your local machine. Use the command below:
```
git clone https://github.com/username/eros-view.git
```

### Step 2: Navigate to the Directory

Navigate to the cloned repository's directory using the command:
```
cd eros-view
```

### Step 3: Install the Package

Install the package using pip. Run the command:

```
pip install .
```

### Step 4: Verify Installation

After installation, you can verify if Eros-View was installed correctly. Run the command:
```
eros-view --help
```
If the installation was successful, this command should show the help menu of Eros-View.


## Installation from binary

### Step 1: Download the Binary

You can download the binary directly from the GitHub Releases page. Choose the binary that matches your operating system and architecture.

### Step 2: Make the Binary Executable

After downloading, you need to make the binary executable. Here is how you do it for different operating systems:

- **Linux/MacOS**: Open a terminal and navigate to the directory where you downloaded the binary. Run the following command to make the binary executable:

    ```
    chmod +x ./eros-view
    ```

- **Windows**: The binary should be executable by default. If it isn't, you may need to unblock it. Right-click the file, select Properties, and then check the box that says 'Unblock'.

### Step 3: Move the Binary to the Appropriate Directory

Next, you should move the binary to a directory in your PATH. Here's how you do it:

- **Linux/MacOS**: Use the following command to move the binary to /usr/local/bin:

    ```
    sudo mv ./eros-view /usr/local/bin/
    ```

- **Windows**: You should add the binary's directory to your PATH. Open System Properties, go to 'Advanced system settings', then 'Environment Variables'. Add the directory of the binary to the 'Path' variable.

### Step 4: Verify Installation

After installation, you can verify if Eros-View was installed correctly. Run the command:

```
eros-view --help
```
If the installation was successful, this command should show the help menu of Eros-View.


## Usage

This program provides command line interfaces for UART, UDP and TCP channels.

### UART

To open a UART channel, use the `uart` command with the following syntax:

```
eros-view uart [CHANNEL] --port [PORT] --baud [BAUD_RATE] --vid [VENDOR_ID]
```
Arguments:
- `[CHANNEL]`: Channel number (default is 1)
- `[PORT]`: Port for UART communication (default is "auto")
- `[BAUD_RATE]`: Baud rate for UART communication (default is 2000000)
- `[VENDOR_ID]`: Vendor ID for automatic serial port detection (default is 4292)

### UDP

To open a UDP channel, use the `udp` command with the following syntax:
```
eros-view udp [CHANNEL] --ip [IP_ADDRESS] --port [PORT]
```

Arguments:
- `[CHANNEL]`: Channel number
- `[IP_ADDRESS]`: IP address for UDP communication (default is "192.168.0.1")
- `[PORT]`: Port for UDP communication (default is 5555)

### TCP

To open a TCP channel, use the `tcp` command with the following syntax:

```
eros-view tcp [CHANNEL] --ip [IP_ADDRESS] --port [PORT]
```


Arguments:
- `[CHANNEL]`: Channel number
- `[IP_ADDRESS]`: IP address for TCP communication (default is "192.168.0.1")
- `[PORT]`: Port for TCP communication (default is 6666)


