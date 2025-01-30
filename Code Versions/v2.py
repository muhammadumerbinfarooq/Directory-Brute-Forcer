import requests
import threading
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Target URL
url = "http://example.com"

# List of directories to check (can be loaded from a file)
directories = [
    "admin",
    "login",
    "dashboard",
    "config",
    "backup"
]

# Function to brute force directories
def check_directory(full_url):
    try:
        response = requests.get(full_url, timeout=5)
        if response.status_code in [200, 403, 401]:
            logging.info(f"Found: {full_url} (Status Code: {response.status_code})")
        else:
            logging.debug(f"Not Found: {full_url} (Status Code: {response.status_code})")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error accessing {full_url}: {e}")

# Function to run brute force with threading
def brute_force_directories(url, directories, threads=5):
    thread_list = []
    for directory in directories:
        full_url = f"{url}/{directory}"
        thread = threading.Thread(target=check_directory, args=(full_url,))
        thread_list.append(thread)
        thread.start()
        
        # Limit the number of concurrent threads
        if len(thread_list) >= threads:
            for t in thread_list:
                t.join()
            thread_list = []
            time.sleep(1)  # Rate limiting

    # Join any remaining threads
    for t in thread_list:
        t.join()

# Run the brute force function
brute_force_directories(url, directories)
