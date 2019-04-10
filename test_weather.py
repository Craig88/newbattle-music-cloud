import os
from yahoo_weather.weather import YahooWeather
from yahoo_weather.config.units import Unit
from dotenv import load_dotenv

load_dotenv()

print('Testing Weather...')


my_id = os.getenv('YAHOO_APP_ID')
my_key = os.getenv('YAHOO_API_KEY')
my_secret = os.getenv('YAHOO_API_SECRET')

city_name = "Edinburgh"

weather = YahooWeather(
        APP_ID=my_id,
        api_key=my_key,
        api_secret=my_secret)

weather.get_yahoo_weather_by_city(city_name, Unit.celsius)
print(city_name)
print(weather.condition.text)
print(weather.condition.temperature)

print('End Weather Test')
