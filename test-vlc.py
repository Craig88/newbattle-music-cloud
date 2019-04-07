import vlc
media = vlc.MediaPlayer("audio.mp3")
media.play()

# A bit of a cheat here to allow it to play
while True:
     pass
