from ip_service import *
from weather_service import *
import json

class DirectInfo:
    #MARK: Get Temp
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

    def get_temperature_from_forecast(forecast):
        try: return int(forecast['current']['temp_c'])
        except: return None 

    #MARK: Get forecast    
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
    
    def get_forecast_from_forecast(forecast):
        try:
            retrived_data = forecast
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
    

    #MARK: Get UV
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

    def get_uv_from_forecast(forecast):
        try:
            retrived_data = forecast['current']['uv']
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

    #MARK: Get Sunrise/Sunset    
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
    
    def get_sunrise_sunset_from_forecast(forecast):
        try:
            retrieved_data = forecast['forecast']['forecastday'][0]['astro']
            return {
                'sunrise':retrieved_data['sunrise'],
                'sunset':retrieved_data['sunset']
            }
        except:
            return None

    #MARK: Get humidity
    def get_humidity_from_location(location: str): # Get humidity
        try: return f"{WeatherService.get_current_weather(location)['current']['humidity']}%"
        except: return None 

    def get_humidity_from_ip():
        try: return f"{WeatherService.get_current_weather(IPService.get_location_only())['current']['humidity']}%"
        except: return None 

    def get_humidity_from_forecast(forecast):
        try: return f"{forecast['current']['humidity']}%"
        except: return None 

    #MARK: Get wind
    def get_wind_from_location(location: str): # Get wind
        try: return f"{int(WeatherService.get_current_weather(location)['current']['gust_kph'])} kph"
        except: return None 

    def get_wind_from_ip():
        try: return f"{int(WeatherService.get_current_weather(IPService.get_location_only())['current']['gust_kph'])} kph"
        except: return None 

    def get_wind_from_forecast(forecast):
        try: return f"{int(forecast['current']['gust_kph'])} kph"
        except: return None 

    #MARK: Get pressure
    def get_pressure_from_location(location:str): # Get pressure
        try: return f"{int(WeatherService.get_current_weather(location)['current']['pressure_mb'])} mb"
        except: return None 

    def get_pressure_from_ip():
        try: return f"{int(WeatherService.get_current_weather(IPService.get_location_only())['current']['pressure_mb'])} mb"
        except: return None 

    def get_pressure_from_forecast(forecast):
        try: return f"{int(forecast['current']['pressure_mb'])} mb"
        except: return None 

    #MARK: Get visibility 
    def get_visibility_from_location(location: str): # Get vis
        try: return f"{int(WeatherService.get_current_weather(location)['current']['vis_km'])} km"
        except: return None 

    def get_visibility_from_ip():
        try: return f"{int(WeatherService.get_current_weather(IPService.get_location_only())['current']['vis_km'])} km"
        except: return None 
    
    def get_visibility_from_forecast(forecast):
        try: return f"{int(forecast['current']['vis_km'])} km"
        except: return None 

    #MARK: Search
    def search(query): 
        try: return WeatherService.search(query)
        except: return None
    
    #MARK: USE THIS!! [facade]
    def get_weather_information_from_location(location: str):
        try: 
            forecast = WeatherService.get_forecast(location)
            build = {
                'current_temp':DirectInfo.get_temperature_from_forecast(forecast),
                'forecast':DirectInfo.get_forecast_from_forecast(forecast),
                'sunrise_sunset':DirectInfo.get_sunrise_sunset_from_forecast(forecast),
                'humidity':DirectInfo.get_humidity_from_forecast(forecast),
                'wind':DirectInfo.get_wind_from_forecast(forecast),
                'pressure':DirectInfo.get_pressure_from_forecast(forecast),
                'visibility':DirectInfo.get_visibility_from_forecast(forecast)
            }
            return build
        except:
            return None

    def get_weather_information_from_ip():
        try:
            forecast = WeatherService.get_forecast(IPService.get_location_only())
            build = {
                'current_temp':DirectInfo.get_temperature_from_forecast(forecast),
                'forecast':DirectInfo.get_forecast_from_forecast(forecast),
                'sunrise_sunset':DirectInfo.get_sunrise_sunset_from_forecast(forecast),
                'humidity':DirectInfo.get_humidity_from_forecast(forecast),
                'wind':DirectInfo.get_wind_from_forecast(forecast),
                'pressure':DirectInfo.get_pressure_from_forecast(forecast),
                'visibility':DirectInfo.get_visibility_from_forecast(forecast)
            }
            return build
        except:
            return None
        

