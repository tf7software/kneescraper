# KneeScraper Instructions

## Overview

**KneeScraper** is a Python script that allows you to scrape a root domain, search for specific pages, and extract data such as emails, phone numbers, or sequences of numbers. The results are saved to a CSV file, and you can stop the script early if needed.

## Prerequisites

Ensure you have the following installed:
- **Python 3.x**: The script requires Python 3.
- **Python packages**: `requests`, `beautifulsoup4`, `pandas`, and `tqdm`.

## Installation Instructions

### Windows

1. **Install Python 3**:
   - Download the Python installer from [python.org](https://www.python.org/downloads/).
   - Run the installer and check the box that says "Add Python to PATH".
   - Follow the prompts to complete the installation.

2. **Open Command Prompt**:
   - Press `Win + R`, type `cmd`, and press Enter.

3. **Install Required Packages**:
   ```bash
   pip install requests beautifulsoup4 pandas tqdm
   ```

4. **Download the Script**:
   - Go to the GitHub repository: [KneeScraper GitHub](https://github.com/tf7software/kneescraper/)
   - Click on the "Code" button and select "Download ZIP".
   - Extract the ZIP file and locate `main.py`.

5. **Run the Script**:
   - In Command Prompt, navigate to the directory where you extracted `main.py` using the `cd` command.
   - Run the script with:
     ```bash
     python main.py
     ```

### macOS

1. **Install Python 3**:
   - Open the Terminal application (found in Applications > Utilities).
   - You can use Homebrew to install Python 3. If you don't have Homebrew installed, first install it from [brew.sh](https://brew.sh/).
   - Install Python 3 using Homebrew:
     ```bash
     brew install python
     ```

2. **Install Required Packages**:
   ```bash
   pip3 install requests beautifulsoup4 pandas tqdm
   ```

3. **Download the Script**:
   - Go to the GitHub repository: [KneeScraper GitHub](https://github.com/tf7software/kneescraper/)
   - Click on the "Code" button and select "Download ZIP".
   - Extract the ZIP file and locate `main.py`.

4. **Run the Script**:
   - In Terminal, navigate to the directory where you extracted `main.py` using the `cd` command.
   - Run the script with:
     ```bash
     python3 main.py
     ```

### Linux

1. **Install Python 3**:
   - Open a terminal window.
   - Most Linux distributions come with Python 3 pre-installed. If not, install it using your package manager:
     ```bash
     sudo apt-get update
     sudo apt-get install python3
     ```

2. **Install Required Packages**:
   ```bash
   pip3 install requests beautifulsoup4 pandas tqdm
   ```

3. **Download the Script**:
   - Go to the GitHub repository: [KneeScraper GitHub](https://github.com/tf7software/kneescraper/)
   - Click on the "Code" button and select "Download ZIP".
   - Extract the ZIP file and locate `main.py`.

4. **Run the Script**:
   - In the terminal, navigate to the directory where you extracted `main.py` using the `cd` command.
   - Run the script with:
     ```bash
     python3 main.py
     ```

## Usage

1. **Run the Script**:
   - Follow the prompts to input the base domain URL, keywords (if any), number of entries, and any extraction options.

2. **Stopping Early**:
   - Type `*FIN` in the terminal at any time to stop the script early and save the results collected so far.

3. **Results**:
   - Results will be saved to a file named `scraped_pages.csv` in the same directory as the script.

## Troubleshooting

- **ModuleNotFoundError**: Ensure that all required packages are installed.
- **Network Errors**: Verify your internet connection and ensure the base URL is accessible.
- **Invalid Extraction Options**: Ensure that extraction options are entered correctly as `'emails'`, `'phone'`, `'numbers'`, or left blank.

---

Feel free to follow these instructions for installing and running the KneeScraper script on your operating system. For more details, contact tf7software using the link in bio
