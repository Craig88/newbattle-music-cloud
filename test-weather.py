from yahoo_weather.weather import YahooWeather
from yahoo_weather.config.units import Unit

weather = YahooWeather(
        APP_ID="DIpksy4o",
        api_key="dj0yJmk9VUc1S3dWQndyYzVmJnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTUz",
        api_secret="63d81895f2ac41afcb5a1db552a74714bf1e00f2")

weather.get_yahoo_weather_by_city("Glasgow", Unit.celsius)
print(weather.condition.text)
print(weather.condition.temperature)
