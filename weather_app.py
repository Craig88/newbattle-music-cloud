import os
from yahoo_weather.weather import YahooWeather

# Get the API credentials, these were loaded in from the .env file
my_id = os.getenv('YAHOO_APP_ID')
my_key = os.getenv('YAHOO_API_KEY')
my_secret = os.getenv('YAHOO_API_SECRET')


def weather_setup():
    """ Connects to the Yahoo Weather API. """
    weather = YahooWeather(
            APP_ID=my_id,
            api_key=my_key,
            api_secret=my_secret)
    return weather
