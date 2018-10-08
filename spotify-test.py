import spotipy
import spotipy.util as util
from playsound import playsound

username = "***REMOVED***"
scope = 'user-library-read'
umbrella = 'spotify:track:5i66xrvSh1MjjyDd6zcwgj'
sunny = "spotify:track:3pf96IFggfQuT6Gafqx2rt"
clouds = "spotify:track:5atQ2haKP5LT65WM0KUts3"

token = util.prompt_for_user_token(username, scope, client_id='***REMOVED***',client_secret='***REMOVED***',redirect_uri='http://localhost/')

sp = spotipy.Spotify(auth=token)

track = sp.track(clouds)

#print(track)
preview_track = track['preview_url']
print(preview_track)
playsound(preview_track)
