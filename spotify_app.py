import spotipy
import spotipy.util as util
import os
import vlc
import time
from dotenv import load_dotenv

load_dotenv()


username = os.getenv('SPOTIFY_USERNAME')
my_id = os.getenv('SPOTIFY_CLIENT_ID')
my_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
scope = 'user-library-read'

showers_track = 'spotify:track:5i66xrvSh1MjjyDd6zcwgj'
sunny_track = 'spotify:track:3pf96IFggfQuT6Gafqx2rt'
cloudy_track = 'spotify:track:5icOoE6VgqFKohjWWNp0Ac'

debug_mode = False  # set to True to turn on a debugging mode


def spotify_setup():
    """ connects to Spotify using the API """
    token = util.prompt_for_user_token(username, scope,
                                       client_id=my_id,
                                       client_secret=my_secret,
                                       redirect_uri='http://localhost/')

    if (token):
        global sp
        sp = spotipy.Spotify(auth=token)
        print("Spotify has been setup")


def play_track_for_weather(weather):
    print("This plays the track for the weather")
    print(weather.text)

    if weather.text == "Sunny" or (debug_mode):
        print("We need to play a Sunny track")
        track = sp.track(sunny_track)
        preview_track = track['preview_url']
        print(preview_track)
        track = vlc.MediaPlayer(preview_track)
        track.play()

    elif weather.text == "Showers":
        print("We need to play a Showers track")
        track = sp.track(showers_track)
        preview_track = track['preview_url']
        print(preview_track)
        track = vlc.MediaPlayer(preview_track)
        track.play()

    else:
        print("Not a recognised weather condition")
        return

    while True:
        time.sleep(1)
        print("Checking state..")
        print(track.get_state())
        if (str(track.get_state()) == "State.Ended"):
            print("This track has finished now")
            # exit()
            return
