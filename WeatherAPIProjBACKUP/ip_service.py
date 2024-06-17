import requests
import json

APIURL = "http://ipinfo.io/json"

class IPService:
    def get_ip_api(): # Return the full API
        try:
            fetched_data = requests.get(url=APIURL).json()
            return fetched_data
        except:
            return None
    
    def get_ip_only(): # Get the IP only from the API call
        try: 
            fetched_data = requests.get(url=APIURL).json()
            return fetched_data["ip"]
        except:
            return None

    def extract_ip_only(json_data): # Extract the IP from the API call
        try:
            return json_data["ip"]
        except:
            return None
    
    def get_location_only(): # Get the location only from the API call
        try: 
            fetched_data = requests.get(url=APIURL).json()
            return fetched_data["city"]
        except:
            return None
    
    def extract_location_only(json_data): # Extract the location only from the API call.
        try:
            return json_data["city"]
        except:
            return None


    