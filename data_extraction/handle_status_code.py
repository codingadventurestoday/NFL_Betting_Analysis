import requests
import json
from datetime import datetime

now = datetime.now()
file_path = "./logging/scrapping_log.json"
def write_to_file(file_name, log_entry):
    with open(file_name, "a") as f:
        f.write(json.dumps(log_entry) + "\n")

def log_request(url):
    headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Cache-Control': 'no-cache',  # Tells the server not to cache the response
    'Pragma': 'no-cache',         # Legacy header for cache control
    'Expires': '0',               # Ensures the cache is expired immediately
    }

    try: 
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        log_entry = {
            "datetime" : now.isoformat(),
            "status_code" : response.status_code,
            "url" : url,
        }
        write_to_file(file_path, log_entry)

        return response

    except ConnectionError as ce:
        log_entry = {
            "datetime" : now.isoformat(),
            "status_code" : "None",
            "err" : ce,
            "url" : url,
        }

        write_to_file(file_path, log_entry)
        return None

    except requests.exceptions.HTTPError as he:
        status_code = str(he.response)
        initial_bracket = status_code.index("[")
        closing_bracket = status_code.index("]")
        status_code = status_code[initial_bracket+1:closing_bracket]

        log_entry = {
            "datetime" : now.isoformat(),
            "status_code" : status_code,
            "url" : url,
        }

        write_to_file(file_path, log_entry)
        return None
    
    except requests.exceptions.InvalidSchema as isch:
        print(f"InvalidSchema: The URL {url} has an invalid schema.")
        
        log_entry = {
            "datetime" : now.isoformat(),
            "status_code" : "None",
            "err" : isch,
            "url" : url,
        }

        write_to_file(file_path, log_entry)
        return None

    except requests.exceptions.RequestException as re:
        log_entry = {
            "datetime" : now.isoformat(),
            "status_code" : "None",
            "err" : re,
            "url" : url,
        }

        write_to_file(file_path, log_entry)
        return None
    
    except Exception as e:
        log_entry = {
            "datetime" : now.isoformat(),
            "status_code" : "None",
            "err" : e,
            "url" : url,
        }

        write_to_file(file_path, log_entry)
        return None