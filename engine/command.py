import time

import pyttsx3
import speech_recognition as sr
import eel

# from engine.features import openCommand

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if len(voices) > 1:
        engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()


# @eel.expose
def takecommand():
    r = sr.Recognizer()
    stop_words = ["stop", "quit", "exit", "ok", "done"]

    with sr.Microphone() as source:
        # print("Adjusting for noise...")
        r.adjust_for_ambient_noise(source)

        print("Listening ...")
        eel.DisplayMessage("Listening")
        while True:
            try:
                audio = r.listen(source, timeout=5)
                print("Recognizing...")
                eel.DisplayMessage("Recognizing... ")
                query = r.recognize_google(audio, language='en-in').lower()
                print(f"User said:{query}")
                eel.DisplayMessage(query)

                # Check for stop words
                if any(word in query for word in stop_words):
                    speak("Stopping now.")
                    eel.ShowHood()
                    print("Execution end")
                    return None
                    # r.pause_threshold = 1
                    # break
                return query
            
                                 # You can process command here
                # speak(f"You said {query}")  #you can uncommand this if want to repeat from jarvis
            except sr.WaitTimeoutError:
                print("No speech detected...")
                continue
            except Exception as e:
                print("Error:", e)
                continue
    
# text = takecommand() 
# if text: # we can directly call the func but this is safer , suppose there is no text then engine tries to speak it get fails or take unnecessary time 
#      speak(text)


@eel.expose
def allCommands():
    try:    
        query = takecommand()

        if not query:
            return

        print(query)
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        elif "on youtube":
            from engine.features import PlayYoutube
            PlayYoutube(query)
        else:
            print("Command not recognized")
            allCommands()
    except sr.WaitTimeoutError:
        print("No speech detected...")
        speak("Could you repeat?")
        eel.DisplayMessage("Could you repeat?")
        

    except Exception as e:
        print("Error:", e)
        speak("Could you repeat?")
        eel.DisplayMessage("Could you repeat?")
        
    # time.sleep(2)
    # eel.ShowHood()