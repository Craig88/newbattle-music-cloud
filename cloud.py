from yahoo_weather.weather import YahooWeather
from yahoo_weather.config.units import Unit
import spotify_app
import weather_app

print("Newbattle Sound Cloud App started")
# Set up Spotify and Weather
spotify_app.spotify_setup()  # Connects to Spotify API
weather = weather_app.weather_setup() # Connects to Yahoo Weather API

# Get the weather data about a particular city
weather.get_yahoo_weather_by_city("Glasgow", Unit.celsius)
print("The city is set to %s" % weather.location.city)
print("The weather conditions are currently %s" % weather.condition.text)
print("The weather status code is %s" % weather.condition.code)
print("The temperature is %s" % weather.condition.temperature)
print("Sunrise is at: %s" % weather.current_observation.astronomy.sunrise)
print("Sunset is at: %s" % weather.current_observation.astronomy.sunset)


# Use Spotify API to play a track based on the weather conditions
spotify_app.play_track_for_weather(weather.condition)

# End the program
print("Newbattle Sound Cloud App finished")
