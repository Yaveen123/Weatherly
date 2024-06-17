from ip_service import *
from weather_service import *
import json
from datetime import datetime

class DirectInfo:
    def get_temperature_from_specified_location(location: str): # Get temp
        try:
            return int(WeatherService.get_current_weather(location)['current']['temp_c'])
        except: 
            return None
        
    def get_temperature_from_ip():
        try:
            return int(WeatherService.get_current_weather(IPService.get_location_only())['current']['temp_c'])
        except:
            return None
        
    def get_forecast_from_specified_location(location: str):# Get Forecast Next Few Hours
        try:
            retrived_data = WeatherService.get_forecast(location)
            return {
                3:int(retrived_data['forecast']['forecastday'][0]['hour'][3]['temp_c']),
                6:int(retrived_data['forecast']['forecastday'][0]['hour'][6]['temp_c']),
                9:int(retrived_data['forecast']['forecastday'][0]['hour'][9]['temp_c']),
                12:int(retrived_data['forecast']['forecastday'][0]['hour'][12]['temp_c']),
                15:int(retrived_data['forecast']['forecastday'][0]['hour'][15]['temp_c']),
                18:int(retrived_data['forecast']['forecastday'][0]['hour'][18]['temp_c']),
                21:int(retrived_data['forecast']['forecastday'][0]['hour'][21]['temp_c'])
            }
        except:
            return None
    
    def get_forecast_from_ip():
        try:
            retrived_data = WeatherService.get_forecast(IPService.get_location_only())
            return {
                3:int(retrived_data['forecast']['forecastday'][0]['hour'][3]['temp_c']),
                6:int(retrived_data['forecast']['forecastday'][0]['hour'][6]['temp_c']),
                9:int(retrived_data['forecast']['forecastday'][0]['hour'][9]['temp_c']),
                12:int(retrived_data['forecast']['forecastday'][0]['hour'][12]['temp_c']),
                15:int(retrived_data['forecast']['forecastday'][0]['hour'][15]['temp_c']),
                18:int(retrived_data['forecast']['forecastday'][0]['hour'][18]['temp_c']),
                21:int(retrived_data['forecast']['forecastday'][0]['hour'][21]['temp_c'])
            }
        except:
            return None
    
    def get_uv_from_location(location: str): # Get Location
        try:
            retrived_data = WeatherService.get_current_weather(location)['current']['uv']
            if retrived_data <= 4:
                return 'Low'
            elif retrived_data <= 6:
                return 'Med'
            elif retrived_data <= 9:
                return 'High'
            else:
                return 'Max' 
        except:
            return None
    
    def get_uv_from_ip():
        try:
            retrived_data = WeatherService.get_current_weather(IPService.get_location_only())['current']['uv']
            if retrived_data <= 4:
                return 'Low'
            elif retrived_data <= 6:
                return 'Med'
            elif retrived_data <= 9:
                return 'High'
            else:
                return 'Max' 
        except:
            return None
        
    def get_sunrise_sunset_from_location(location: str): # Get sunrise/sunset
        try:
            retrieved_data = WeatherService.get_astronomy(location)
            return {
                'sunrise':retrieved_data['astronomy']['astro']['sunrise'],
                'sunset':retrieved_data['astronomy']['astro']['sunset']
            }
        except:
            return None
    
    def get_sunrise_sunset_from_ip():
        try:
            retrieved_data = WeatherService.get_astronomy(IPService.get_location_only())
            return {
                'sunrise':retrieved_data['astronomy']['astro']['sunrise'],
                'sunset':retrieved_data['astronomy']['astro']['sunset']
            }
        except:
            return None
    
    def get_humidity_from_location(location: str): # Get humidity
        return f"{WeatherService.get_current_weather(location)['current']['humidity']}%"

    def get_humidity_from_ip():
        return f"{WeatherService.get_current_weather(IPService.get_location_only())['current']['humidity']}%"

    def get_wind_from_location(location: str): # Get wind
        return f"{int(WeatherService.get_current_weather(location)['current']['gust_kph'])} kph"
    
    def get_wind_from_ip():
        return f"{int(WeatherService.get_current_weather(IPService.get_location_only())['current']['gust_kph'])} kph"
    
    def get_pressure_from_location(location:str): # Get pressure
        return f"{int(WeatherService.get_current_weather(location)['current']['pressure_mb'])} mb"
    
    def get_pressure_from_ip():
        return f"{int(WeatherService.get_current_weather(IPService.get_location_only())['current']['pressure_mb'])} mb"
    
    def get_visibility_from_location(location: str): # Get vis
        return f"{int(WeatherService.get_current_weather(location)['current']['vis_km'])} km"

    def get_visibility_from_ip():
        return f"{int(WeatherService.get_current_weather(IPService.get_location_only())['current']['vis_km'])} km"



