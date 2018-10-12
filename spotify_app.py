import spotipy
import spotipy.util as util
import os
from playsound import playsound
from dotenv import load_dotenv

load_dotenv()

username = os.getenv('USERNAME')
my_id = os.getenv('CLIENT_ID')
my_secret = os.getenv('CLIENT_SECRET')
scope = 'user-library-read'

umbrella = 'spotify:track:5i66xrvSh1MjjyDd6zcwgj'
sunny = 'spotify:track:3pf96IFggfQuT6Gafqx2rt'
cloudy_track = 'spotify:track:5atQ2haKP5LT65WM0KUts3'


def spotify_setup():
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
    if weather.text == "Cloudy":
        print("We need to play a cloudy track")
        track = sp.track(cloudy_track)
        preview_track = track['preview_url']
        print(preview_track)
        playsound(preview_track, block=False)  # don't block it!
