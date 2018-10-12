from weather import Weather, Unit
import pgzrun

WIDTH = 400
HEIGHT = 400

print('Sound Cloud App')

weather = Weather(unit=Unit.CELSIUS)
condition = location.condition
location = weather.lookup_by_location('Perth, WA')


def draw():
    screen.clear()
    screen.fill('blue')
    screen.draw.text(weather_condition.text, (20, 100))

pgzrun.go()
