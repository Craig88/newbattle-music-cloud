from weather import Weather, Unit
import pgzrun
import os
import spotify_app

WIDTH = 400
HEIGHT = 400

print('Sound Cloud App')
spotify_app.spotify_setup()

weather = Weather(unit=Unit.CELSIUS)
location = weather.lookup_by_location('Perth, WA')
weather_condition = location.condition
spotify_app.play_track_for_weather(weather_condition)


def draw():
    screen.clear()
    screen.fill('blue')
    screen.draw.text(weather_condition.text, (20, 100))

pgzrun.go()
