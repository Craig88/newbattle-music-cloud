from yahoo_weather.weather import YahooWeather
from yahoo_weather.config.units import Unit
import pgzrun
import spotify_app
import weather_app

WIDTH, HEIGHT = 400, 400

print("Sound Cloud App")
spotify_app.spotify_setup()
weather = weather_app.weather_setup()

weather.get_yahoo_weather_by_city("Glasgow", Unit.celsius)
print(weather.condition.text)
print(weather.condition.temperature)

weather_condition = weather.condition
spotify_app.play_track_for_weather(weather_condition)


def draw():
    screen.clear()
    screen.fill('blue')
    screen.draw.text('Sound Cloud App', (0, 0))
    screen.draw.text(weather_condition.text, (100, 100))


pgzrun.go()
