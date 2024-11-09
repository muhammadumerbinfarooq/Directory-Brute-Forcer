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
