import os
from yahoo_weather.weather import YahooWeather
from yahoo_weather.config.units import Unit
from dotenv import load_dotenv

load_dotenv()

id = os.getenv('YAHOO_APP_ID')
key = os.getenv('YAHOO_API_KEY')
secret = os.getenv('YAHOO_API_SECRET')

city_name = "Glasgow"

weather = YahooWeather(
        APP_ID=id,
        api_key=key,
        api_secret=secret)

weather.get_yahoo_weather_by_city(city_name, Unit.celsius)
print(city_name)
print(weather.condition.text)
print(weather.condition.temperature)
