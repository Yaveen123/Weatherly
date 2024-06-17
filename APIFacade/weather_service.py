import requests
import json

# Use api key. Reset key at: https://www.weatherapi.com/my/ 
KEY = 'KEY'

# API Url to call from. Maximum 5 million calls for the first month, and then 1 million class after that.

class WeatherService:
    def error_capture(json_data): 
        try: # If the API returned an error, then code will pass.
            if json_data['error'] == '': 
                pass
            return None # Always return none when error
        except:
            return json_data

    def get_current_weather(query): # Get all the data from the API 
        try:
            api_url = "http://api.weatherapi.com/v1/current.json"
            api_params = {
                'key':KEY,          # API Access Key.
                'q':query,        # Search for this location. 
            }
            fetched_data = requests.get(url=api_url, params=api_params).json()
            return WeatherService.error_capture(fetched_data)
        except:
            return None
    
    def get_forecast(query): # Get all the data from the API 
        try:
            api_url = "http://api.weatherapi.com/v1/forecast.json"
            api_params = {
                'key':KEY,          # API Access Key.
                'q':query,        # Search for this location. 
                'days':1,
                'alerts':'yes',
                'aqi':'yes'
            }
            fetched_data = requests.get(url=api_url, params=api_params).json()
            return WeatherService.error_capture(fetched_data)
        except:
            return None
    
    def search(query): # Get all the data from the API 
        try:
            api_url = "http://api.weatherapi.com/v1/search.json"
            api_params = {
                'key':KEY,          # API Access Key.
                'q':query,        # Search for this location. 
            }
            fetched_data = requests.get(url=api_url, params=api_params).json()
            return WeatherService.error_capture(fetched_data)
        except:
            return None
    
    def get_astronomy(query): # Get all the data from the API
        try:
            api_url = "http://api.weatherapi.com/v1/astronomy.json"
            api_params = {
                'key':KEY,          # API Access Key.
                'q':query,        # Search for this location. 
            }
            fetched_data = requests.get(url=api_url, params=api_params).json()
            return WeatherService.error_capture(fetched_data)
        except:
            return None


