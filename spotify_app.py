import spotipy
import spotipy.util as util
import os
import vlc
import time
from dotenv import load_dotenv

load_dotenv()  # Get the credentials from the .env file

# Set the API credentials, these were loaded in from the .env file
username = os.getenv('SPOTIFY_USERNAME')
my_id = os.getenv('SPOTIFY_CLIENT_ID')
my_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
scope = 'user-library-read'

# Links to tracks on Spotify
# https://community.spotify.com/t5/Spotify-Answers/What-s-a-Spotify-URI/ta-p/919201

debug_track = "spotify:track:3UL6Lzsocv9Ucizgzid2B0"  # We Like To Party by Venga Boys
showers_track = "spotify:track:5i66xrvSh1MjjyDd6zcwgj"  # Umbrella by Rihanna
sunny_track = "spotify:track:3UL6Lzsocv9Ucizgzid2B0"  # We Like To Party by Venga Boys
cloudy_track = "spotify:track:3xhhsvui4g3hkMtA89f2uX"  # Cloudbusting by Just Us
fog_track = "spotify:track:4rhUBIlzi7zgV7TryhVujl" # Edge of Darkness by Greta van Fleet

debug_mode = True  # set to True to turn on a debugging mode


def spotify_setup():
    """ connects to Spotify using the API """

    # attempts to connect to Spotify API,
    # if successful it Spotify gives us a token
    token = util.prompt_for_user_token(username, scope,
                                       client_id=my_id,
                                       client_secret=my_secret,
                                       redirect_uri='http://localhost/')

    if (token):
        global sp
        sp = spotipy.Spotify(auth=token)
        print("Spotify has been setup")


def play_track_for_weather(weather):
    """ Plays a song from Spotify based on the current weather """

    print("This plays the track for the weather %s" % weather.text)
    print("This plays the track for the condition code %s" % weather.code)

    # Yahoo! weather condition codes found at
    # https://developer.yahoo.com/weather/documentation.html#codes

    if (debug_mode):
        print("Debug mode - Playing debug track")
        track = sp.track(fog_track)  # Get the track from Spotify
        preview_track = track['preview_url']  # Get the link to the 30 second clip
        song = vlc.MediaPlayer(preview_track)
        song.play()  # Play the 30 second clip

    elif weather.code == 32:  # Code 32: Sunny
        print("We need to play a Sunny track")
        track = sp.track(sunny_track)
        preview_track = track['preview_url']
        print(preview_track)
        song = vlc.MediaPlayer(preview_track)
        song.play()

    elif weather.code == 11:  # Code 11: Showers
        print("We need to play a Showers track")
        track = sp.track(showers_track)
        preview_track = track['preview_url']
        print(preview_track)
        song = vlc.MediaPlayer(preview_track)
        song.play()

    elif weather.code == 28:  # Code 28: Mostly Cloudy (day)
        print("We need to play a Mostly Cloudy")
        track = sp.track(cloudy_track)
        preview_track = track['preview_url']
        print(preview_track)
        song = vlc.MediaPlayer(preview_track)
        song.play()

    elif weather.code == 20:  # Code 20: Fog
        print("We need to play a Fog track")
        track = sp.track(fog_track)
        preview_track = track['preview_url']
        print(preview_track)
        song = vlc.MediaPlayer(preview_track)
        song.play()

    else:
        print("Not a recognised weather code.")
        return

    while True:  # This loops repeats until the song has stopped playing
        time.sleep(1)  # wait a second
        print("Checking state...")
        print(song.get_state())
        if (str(song.get_state()) == "State.Ended"):  # if the song has ended
            print("This song has finished now")
            return
