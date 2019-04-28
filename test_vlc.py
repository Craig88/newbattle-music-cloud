import vlc
import time

print("Testing VLC player...")

# Sample of a Chvrches song
mp3_url = "https://p.scdn.co/mp3-preview/9fbeaa5db69e171ed646374d1da92bdde74044ad?cid=f4e4247d61054c97aab361f9f95a06e0"

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
        break
