from weather import Weather, Unit
import pgzrun

WIDTH = 400
HEIGHT = 400


print("Sound Cloud App")

weather = Weather(unit=Unit.CELSIUS)
location = weather.lookup_by_location('Edinburgh, UK')
condition = location.condition


def draw():
    screen.clear()
    screen.fill("blue")
    screen.draw.text(condition.text, (20, 100))


pgzrun.go()
