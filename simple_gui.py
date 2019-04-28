from guizero import App, PushButton
from subprocess import call


def main_pressed():
    call(['python3', 'cloud.py'])


def weather_pressed():
    call(['python3', 'test_weather.py'])


def vlc_pressed():
    call(['python3', 'test_vlc.py', '&'])


app = App(title="Newbattle Sound Cloud")
main_button = PushButton(app, text="Run Sound Cloud", command=main_pressed)
button1 = PushButton(app, text="Test Weather", command=weather_pressed)
button2 = PushButton(app, text="Test VLC", command=vlc_pressed)
app.display()
