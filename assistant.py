# import os, time
import playsound
# import pyaudio
import time
import speech_recognition as sr
from gtts import gTTS
import pyautogui as p


# pygame.mixer.init()
# pygame.mixer.music.load("song.mp3")
# pygame.mixer.music.play()
# playsound.playsound(r"C:\Users\Stephen Dapaah\PycharmProjects\hello\song.mp3")
# playsound.playsound(r"E:\music\Music\Christopher_Martin_-_Paper_Lovin.mp3")
# playsound.playsound(r"C:\Users\Stephen Dapaah\Documents\Sound_recordings\word.m4a")
# playsound.playsound("word.m4a")
def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print("You said: {}".format(said))

        except sr.UnknownValueError:
            print("Google Speech Recognition couldn't understand the audio")
            program(get_audio())

        except sr.RequestError as v:
            print("could not request results from Google Speech Recognition service: {}".format(v))
            print("Shutting Down....")
            quit()

    return said


speak("hello there! my name is Jarvis. Please Say something")


def program(said):
    if "hello" in said:
        speak("hello there! my name is Jarvis. I am a personal assistant to Dr. Stephen. How may I help you?")
    if "what is your name" in said:
        speak("My name is Jarvis")
    if "what says the time" in said:
        speak("The time is{}".format(time.ctime()))
    if "how are you doing" in said:
        speak("By the  Grace of God I am fine")
    if "have you eaten" in said:
        speak("I am always full so far as i have electricity")
    if "open word" in said:
        print("Opening Microsoft Word...")
        playsound.playsound("word.m4a")
        p.moveTo(69, 748)
        p.click()
        p.typewrite("word")
        p.press("enter")
    if "open excel" in said:
        print("Opening Microsoft Excel...")
        p.moveTo(69, 748)
        p.click()
        p.typewrite("excel")
        p.press("enter")
    if "open powerpoint" in said:
        print("Opening Microsoft Power Point...")
        p.moveTo(69, 748)
        p.click()
        p.typewrite("powerpoint")
        p.press("enter")
    if "open chrome" in said:
        print("Opening Google Chrome...")
        p.moveTo(69, 748)
        p.click()
        p.typewrite("chrome")
        p.press("enter")
    if "open excel" in said:
        print("Opening Microsoft Excel...")
        p.moveTo(69, 748)
        p.click()
        p.typewrite("excel")
        p.press("enter")
    if "open file manager" in said:
        print("Opening File Explorer...")
        p.moveTo(69, 748)
        p.click()
        p.typewrite("file")
        p.press("enter")
    if "open note pad" in said:
        print("Opening notepad...")
        p.moveTo(69, 748)
        p.click()
        p.typewrite("excel")
        p.press("enter")
    if "open corel draw" in said:
        print("Opening Corel Draw...")
        p.moveTo(69, 748)
        p.click()
        p.typewrite("corel")
        p.press("enter")
    if "open photoshop" in said:
        print("Opening Adobe Photoshop CC 2019...")
        p.moveTo(69, 748)
        p.click()
        p.typewrite("photoshop")
        p.press("enter")


while get_audio() != "shutdown":
    print("Say Something...")
    program(get_audio())
else:
    quit()


