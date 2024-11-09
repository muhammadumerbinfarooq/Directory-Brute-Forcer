# Directory Brute Forcer

A simple Python script to brute force directories on a web server to discover hidden content.

## Features
- Scans a list of directories to find accessible ones
- Prints out found and not found directories

## Requirements
- Python 3.x
- `requests` library

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Directory-Brute-Forcer.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Directory-Brute-Forcer
    ```
3. Install the required library:
    ```bash
    pip install requests
    ```

## Usage
1. Open the script file `brute_force.py`.
2. Replace the `url` variable with the target URL.
3. Add or modify the list of directories in the `directories` list.
4. Run the script:
    ```bash
    python brute_force.py
    ```

## Example
```python
import requests

# Target URL
url = "http://example.com"

# List of directories to check
directories = [
    "admin",
    "login",
    "dashboard",
    "config",
    "backup"
]

# Function to brute force directories
def brute_force_directories(url, directories):
    for directory in directories:
        full_url = f"{url}/{directory}"
        response = requests.get(full_url)
        if response.status_code == 200:
            print(f"Found: {full_url}")
        else:
            print(f"Not Found: {full_url}")

# Run the brute force function
brute_force_directories(url, directories)
