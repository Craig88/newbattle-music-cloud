# newbattle-sound-cloud

*draft in development*

Play music snippets based on current weather conditions. Uses live data from Yahoo Weather and Spotify.

Made with [Newbattle High School](http://www.newbattle.org.uk/) students and the [University of Edinburgh](https://www.de.ed.ac.uk/) as part of the [Everybody Makes The School](https://everybodymakes.com/) project.

#### Python libraries needed:
```sh
pip3 install playsound
pip3 install -U python-dotenv
pip3 install spotipy
pip3 install yahoo-weather
pip3 install pyobjc
pip3 install pygame
pip3 install pgzero
pip3 install python-vlc
```
or (on macOS)

```sh
pip3 install -r requirements.txt
```

#### Other libraries needed

`sudo apt-get install python-gst-1.0`

`sudo apt-get install pulseaudio`

#### API Keys
API keys for Yahoo and Spotify are stored in the `.env` file


#### Speaker test on Raspberry Pi
The following command performs a sound test
```sh
speaker-test -c2
```

#### Switching audio on Raspberry Pi:
The following command will switch the audio output to HDMI:

```sh
amixer cset numid=3 2
```

Here the output is being set to 2, which is HDMI. Setting the output to 1 switches to analogue (headphone jack). The default setting is 0 which is automatic.

### Other useful titbits
Other libraries that might be needed:
gstreamer1.0-plugins-good gstreamer1.0-plugins-ugly gstreamer1.0-tools
