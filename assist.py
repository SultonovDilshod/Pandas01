import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def Hello():
    speak("hello sir I am your desktop assistant. Tell me how may I help you")

if __name__ == '__main__':
    Hello()