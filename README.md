# newbattle-sound-cloud

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
or

```sh
pip install -r requirements.txt
```

#### Other libraries needed

`sudo apt-get install python-gst-1.0`

(might also need? gstreamer1.0-plugins-good gstreamer1.0-plugins-ugly gstreamer1.0-tools)

#### Speaker test
```sh
speaker-test -c2
```
```sh
sudo apt-get install pulseaudio
```


#### Switching audio:
The following command, entered in the command line, will switch the audio output to HDMI:

```sh
amixer cset numid=3 2
```

Here the output is being set to 2, which is HDMI. Setting the output to 1 switches to analogue (headphone jack). The default setting is 0 which is automatic.
