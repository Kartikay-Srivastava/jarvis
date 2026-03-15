import pyttsx3
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    if len(voices) > 1:
        engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate',120)
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=5)
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-IN')
            print("User said:", query)
            return query.lower()
        except Exception as e:
            print("Error:", e)
            return ""

text = takecommand()
if text:  # we can directly call the func but this is safer , suppose there is no text then engine tries to speak it get fails or take unnecessary time
    speak(text)