# Newbattle Music Cloud

<img src="photo-cloud.jpg" width="400">

Made with [Newbattle High School][1] students and the [University of Edinburgh][2] as part of the [Everybody Makes The School][3] project.
Play music snippets based on current weather conditions. Uses live data from Yahoo Weather and Spotify.

### Required Python packages
The `requirements.txt` file lists all the Python packages needed to run the app.
To install them run this command:

```sh
pip3 install -r requirements.txt
```

### Other libraries
Depending on the computer, these libraries may also be needed.
Install them by running these commands:

```sh
sudo apt-get install python-gst-1.0
sudo apt-get install pulseaudio
```

### API Keys
API keys for Yahoo and Spotify are stored in the `.env` file.
Treat these like passwords and keep them secret.

### Testing

Internet connection test:
```sh
ping bbc.co.uk
```

Sound test:
```sh
speaker-test -c2
```
This lets you control the sound levels if they need adjusted:
```sh
alsamixer
```
Weather test:
```sh
python3 test_weather.py
```

VLC test:
```sh
python3 test_vlc.py
```

### Run the app
```sh
python3 cloud.py
```

### Other useful titbits
Other libraries that might be needed:
`gstreamer1.0-tools` `gstreamer1.0-plugins-good` `gstreamer1.0-plugins-ugly` 

### Using Cron to schedule the app

[https://crontab-generator.org/][4]
[https://www.raspberrypi.org/documentation/linux/usage/cron.md][5]

```sh
python3 test_cron.py >> log.txt

python3 /home/pi/Desktop/newbattle-sound-cloud/test_cron.py >> /home/pi/Desktop/newbattle-sound-cloud/log.txt

* * * * * python3 /home/pi/Desktop/newbattle-sound-cloud/test_cron.py >> /home/pi/Desktop/newbattle-sound-cloud/log.txt

* * * * * python3 /home/pi/Desktop/newbattle-sound-cloud/test_vlc.py >> /home/p$
```

[https://developer.yahoo.com/weather/documentation.html][6]

Condition codes [https://developer.yahoo.com/weather/documentation.html#codes][7]


This command switches the audio output to HDMI:
```sh
amixer cset numid=3 2
```

Here the output is set to 2, which is HDMI. Setting the output to 1 switches to analogue (headphone jack). The default setting is 0 which is automatic.


[1]:	http://www.newbattle.org.uk/
[2]:	https://www.de.ed.ac.uk/
[3]:	https://everybodymakes.com/
[4]:	https://crontab-generator.org/
[5]:	https://www.raspberrypi.org/documentation/linux/usage/cron.md
[6]:	https://developer.yahoo.com/weather/documentation.html
[7]:	https://developer.yahoo.com/weather/documentation.html#codes
