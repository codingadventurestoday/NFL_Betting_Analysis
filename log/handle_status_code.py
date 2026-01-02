import requests
import json
import os
from datetime import datetime

def log_request(url):
    logging_dir = "./logging"
    log_file = os.path.join(logging_dir, "scrapping_log.json")

    # Ensure the logging directory exists
    if not os.path.exists(logging_dir):
        os.makedirs(logging_dir)

    request_info = {
        "url": url,
        "timestamp": datetime.now().isoformat(),
        "status_code": None,
        "error": None
    }
    try:
        # Make the GET request
        response = requests.get(url, timeout=600)
        request_info["status_code"] = response.status_code
        print(f"Request to {url} returned status code: {response.status_code}")
        
        logs = []

        # Log the request information
        # log_entry = request_info
        # Read existing logs or start a new list
        if os.path.exists(log_file) and os.path.getsize(log_file) > 0:
            with open(log_file, "r") as f:
                try:
                    logs = json.load(f)
                except json.JSONDecodeError:
                    pass
        
        # Append the new log entry
        logs.append(request_info)

        # Write the updated logs back to the file
        with open(log_file, "w") as f:
            json.dump(logs, f, indent=4)

        return response

    except requests.exceptions.RequestException as e:
        request_info["error"] = str(e)
        request_info["status_code"] = "Error"
        print(f"An error occurred while requesting {url}: {e}")
        
        # Log the error information
        log_entry = request_info
        
        # Read existing logs or start a new list
        if os.path.exists(log_file) and os.path.getsize(log_file) > 0:
            with open(log_file, "r") as f:
                logs = json.load(f)
        else:
            logs = []
            
        # Append the new log entry
        logs.append(log_entry)
        
        # Write the updated logs back to the file
        with open(log_file, "w") as f:
            json.dump(logs, f, indent=4)
  
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None