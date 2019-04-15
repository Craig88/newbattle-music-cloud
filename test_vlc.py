import vlc
import time
import sys

print("Testing VLC player..."")

# Sample of Chvrches song
mp3_url = "https://p.scdn.co/mp3-preview/9fbeaa5db69e171ed646374d1da92bdde74044ad?cid=***REMOVED***"

media = vlc.MediaPlayer(mp3_url)
media.play()

print(media.get_state())

# A bit of a cheat here to allow it to play
while True:
    pass
    time.sleep(1)
    # print("Checking state..")
    # print(media.get_state())
    if (str(media.get_state()) == "State.Ended"):
        print("This is finished now")
        sys.exit()
