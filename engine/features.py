# import playsound as playsound

from playsound import playsound

import eel
# playing assistant sound function 
@eel.expose
def playAssistantSound():
    music_dir="www//assesets//audio//hello.wav"

    playsound(music_dir)

@eel.expose
def playMic():
    music_dir="www//assesets//audio //hello.wav"

    playsound(music_dir)