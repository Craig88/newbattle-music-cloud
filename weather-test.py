from yahoo_weather.weather import YahooWeather
from yahoo_weather.config.units import Unit

weather = YahooWeather(
        APP_ID="***REMOVED***",
        api_key="***REMOVED***",
        api_secret="***REMOVED***")

weather.get_yahoo_weather_by_city("Glasgow", Unit.celsius)
print(weather.condition.text)
print(weather.condition.temperature)
