import pyttsx3
import webbrowser
from selenium import webdriver
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import calendar
import time
import playsound
import pyautogui
from easygui import filesavebox

engine = pyttsx3.init('sapi5')
client = wolframalpha.Client('Your_App_ID')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices) - 3].id)


def speak(audio):
    # print('Jarvis: ' + audio)
    engine.say(audio)
    engine.runAndWait()
    return 'Jarvis: ' + audio


def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if (currentH >= 0) and (currentH < 12):
        return 'Good Morning!\nHow may I help you? \nEnter jarvis commands to get list of commands'

    if (currentH >= 12) and (currentH < 18):
        return 'Good Afternoon!\nHow may I help you? \nEnter jarvis commands to get list of commands'

    if (currentH >= 18) and (currentH != 0):
        return 'Good Evening!\nHow may I help you? \nEnter jarvis commands to get list of commands'


def save(take):
    save_file = filesavebox()
    save1 = open(save_file, "w")
    save1.write(take)
    speak("file saved successfully")


def getdate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]  # e.g. Monday
    monthnum = now.month
    daynum = now.day

    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                   'October', 'November', 'December']
    ordinalnumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th',
                      '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd',
                      '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']
    return 'Today is ' + weekday + ' ' + month_names[monthnum - 1] + ' the ' + ordinalnumbers[daynum - 1] + '.'


def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=7.0)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.RequestError as v:
        print("could not request results from Google Speech Recognition service: {}".format(v))
        query = str(input('Command: '))

    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query


def main(query):
    if 'open youtube' in query:
        webbrowser.open('www.youtube.com')
        return "okay, opening youtube..."

    elif 'open google' in query:
        webbrowser.open('www.google.co.in')
        return 'okay, opening google...'

    elif "what is the time" in query:
        t = time.ctime().split()
        r = t[-2].split(":")
        v = r[:2]
        currentH = int(datetime.datetime.now().hour)
        if (currentH >= 0) and (currentH < 12):
            # speak('Good Morning!')
            v.append("am")
        else:
            hour = int(v[0]) - 12
            v[0] = hour
            v.append("pm")
        #print(v)
        return "The time is {}:{} {}".format(v[0], v[1], v[2])
        #speak(str(v))

    elif "sing birthday song" in query:
        return """happy birthday to you! happy birthday to you!! happy birthday too you!!! How old are you now,"
              How old are you now! May God bless you now, May God bless you now,
              "May God bless you now Hip! Hip!! Hip!!! Hurry!!! """

    elif "take a screenshot" in query:
        # name = input("Enter name of the screenshot\n>>")
        r = random.randrange(1, 1000)
        name = "screenshot{}".format(r)
        fname = "{}.png".format(name)
        speak("You have five seconds to setup the screen")
        time.sleep(5)
        speak("Taking screenshot now...")
        pyautogui.screenshot(fname)
        speak("Screenshot taken. Do you want to show it?")
        try:
            show = myCommand()
            if "yes" in show:
                speak("Showing the image...")
                os.startfile(r"C:\Users\Stephen Dapaah\PycharmProjects\hello\{}".format(fname))
                speak("Image opened")
            else:
                pass
        except OSError as e:
            speak("{}".format(e) + ". Please type in your response")
            show = str(input('Command: '))
            if "yes" in show:
                speak("Showing the image...")
                os.startfile(r"C:\Users\Stephen Dapaah\PycharmProjects\hello\{}".format(fname))
                speak("Image opened")
            else:
                pass

    elif "what are your functions" in query or "jarvis commands" in query:
        handle = open("instructions.txt", "r")
        file1 = handle.read()
        handle.close()
        return file1

    elif "play game" in query:
        pass

    elif "set reminder" in query:
        speak('what do you want me to remind you of?')
        try:
            reminder = myCommand()
        except OSError as e:
            speak("{}".format(e) + ". Please type in the reminder")
            reminder = str(input('Command: '))


        remind1 = open("reminder.txt", "r")
        lines = 0
        for i in remind1:
            lines += 1
        remind = open("reminder.txt", "a")
        if lines == 0:
            remind.write(reminder)
        else:
            remind.write("\n")
            remind.write(reminder)
        remind.close()
        speak("Sure thing! I will remind you")

    elif "show reminders" in query or "do i have any reminders" in query:
        show_reminders = open("reminder.txt", "r")
        show_reminders.seek(0)
        first_char = show_reminders.read(1)
        if not first_char:
            return "You have no reminders at the moment. Say set reminder to set one"
        else:
            show_reminders.seek(0)
            num_of_lines = sum(1 for reminders in show_reminders)
            if num_of_lines == 1:
                return "You have only {} reminder. Which says: ".format(num_of_lines)
            else:
                return "You have {} reminders. These are".format(num_of_lines)
            show_reminders.seek(0)
            for reminders1 in show_reminders:
                speak(reminders1)
            show_reminders.close()

    elif "delete reminder" in query:
        speak('which reminder do you want to delete')
        try:
            delete = myCommand()
        except OSError as e:
            speak("{}".format(e) + ". Please type in the reminder you wish to delete")
            delete = str(input('Command: '))

        if delete == "first":
            num = 0
        elif delete == "second":
            num = 1
        elif delete == "third":
            num = 2
        elif delete == "fourth":
            num = 3
        elif delete == "fifth":
            num = 4
        elif delete == "sixth":
            num = 5
        elif delete == "seventh":
            num = 6
        elif delete == "eighth":
            num = 7
        elif delete == "ninth":
            num = 8
        elif delete == "tenth":
            num = 9


        delete1 = open("reminder.txt", "r")
        lines1 = delete1.readlines()
        delete1.close()
        try:
            del lines1[num]
            new_file = open("reminder.txt", "w+")
            for line in lines1:
                new_file.write(line)
            new_file.close()
            speak("Reminder deleted successfully")
        except IndexError as e:
            speak("That ({}) reminder does not exist".format(delete))
        except Exception as err:
            speak("There was a problem deleting your reminder!!!")

    elif "delete all reminders" in query:
        all = open("reminder.txt", "w")
        all.flush()
        all.close()
        return "All reminders deleted"

    elif "select all" in query:
        pyautogui.hotkey("ctrl", "a")
        return "Text select"

    elif "copy it" in query:
        pyautogui.hotkey("ctrl", "c")
        return "Text copied"

    elif "open notepad" in query:
        # os.startfile(r"%windir%\system32\notepad.exe")
        pyautogui.press("win")
        pyautogui.typewrite("notepad")
        pyautogui.press("enter")
        return "Notepad opened"

    elif "paste it" in query:
        pyautogui.hotkey("ctrl", "v")
        return "Text pasted"

    elif "undo" in query:
        pyautogui.hotkey("ctrl", "z")
        return "Action undone"

    elif "redo" in query:
        pyautogui.hotkey("ctrl", "y")
        return "Action redone"

    elif "scrolldown" in query:
        pyautogui.press("pagedown")
        return "scrolled down"

    elif "scrollup" in query:
        pyautogui.press("pageup")
        return "scrolled up"

    elif "exist edit mode" in query:
        return "Leaving edit mode..."

    elif "what is your name" in query:
        return "My name is Jarvis"

    elif "tell me about yourself" in query:
        return """hello i am jarvis. I am a digital assistant. My creator is Doctor Stephen Dapaah.
         He is a computer scientist. I am developed to make things easier, I can open browser and other applications. 
         I can also play a particular song for you. I am trained to chat formally with users. I was created with Python and I am
         still under development. You can give me commands now"""

    elif "how are you doing" in query:
        return "By the  Grace of God I am fine"

    elif "have you eaten" in query:
        return "I am always full so far as i have electricity"

   # elif query.find("have you eaten food") != -1:
    #    speak("yes please")

    elif "search" in query:
        speak("What do you want to search for?")
        try:
            search = myCommand()
        except OSError as e:
            speak("{}".format(e) + ". Please type in what you want to search for")
            search = str(input('Command: '))
        url = "https://www.google.com/search?q=" + search
        webbrowser.get().open(url)
        speak("This is what google tells me about " + search)

    elif "find a place" in query:
        speak("Where do you want to find?")
        try:
            location = myCommand()
        except OSError as e:
            speak("{}".format(e) + ". Please type in the location")
            location = str(input('Command: '))
        url = "https://www.google.nl/maps/place/" + location + "/&amp;"
        webbrowser.get().open(url)
        speak("here is the location of " + location)

    elif "find someone" in query:
        speak("Who should I find for you?")
        try:
            person = myCommand()
            someone = person.replace(" ", "")
        except OSError as e:
            speak("{}".format(e) + ". Please type in the name")
            person = str(input('Command: '))
        someone = person.replace(" ", "")
        url = "https://web.facebook.com/" + someone
        webbrowser.get().open(url)
        speak("This is who " + person + " is")

    elif "open word" in query:
        speak("opening Microsoft word")
        # os.startfile(r"C:\Users\Stephen Dapaah\PycharmProjects\hello\word.m4a")
        playsound.playsound("word.m4a")
        os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
        return "Microsoft word opened"

    elif "open excel" in query:
        os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")
        return "Opening Microsoft Excel..."

    elif "open powerpoint" in query:
        os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE")
        return "Opening Microsoft Power Point..."

    elif "open chrome" in query:
        os.startfile(r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        return "opening Google chrome..."

    elif "open photoshop" in query:
        os.startfile(r"C:\Program Files\Adobe\Adobe Photoshop CC 2019\Photoshop.exe")
        return "opening adobe photoshop cc 2019..."

    elif 'open gmail' in query:
        webbrowser.open('www.gmail.com')
        return 'okay, opening gmail...'

    elif "what\'s up" in query or 'how are you' in query:
        stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
        return random.choice(stMsgs)

    elif "type something" in query:
        speak("I am listening...")
        try:
            type1 = myCommand()
            os.startfile(r"%windir%\system32\notepad.exe")
            pyautogui.typewrite(type1)
        except OSError as e:
            speak("{}".format(e) + ". Please type in the message")
            type1 = str(input('Command: '))

    elif "hello jarvis" in query or "hey jarvis" in query:
        comments = ["At your service Sir!", "I am online Sir!",
                    "I am activated Sir!", "What can I do for you Sir!",
                    "Talk to me Sir!", "I am awake Sir"]
        r = random.choice(comments)
        return r

    elif "close browser" in query:
        pass

    elif "edit mode" in query:
        pass

    elif 'send email' in query:
        speak('Who is the recipient? ')
        try:
            recipient = myCommand()
        except OSError as e:
            speak("{}".format(e) + ". Please type in the recipient")
            recipient = str(input('Command: '))

        if 'me' in recipient:
            try:
                speak('What should I say? ')
                try:
                    content = myCommand()
                except OSError as e:
                    speak("{}".format(e) + ". Please type in the message")
                    content = str(input('Command: '))

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login("stephendappah1@gmail.com", 'qwerty@1')
                server.sendmail('stephendappah1@gmail.com', "stephen.dapaah@stu.ucc.edu.gh", content)
                server.close()
                speak('Email sent!')

            except:
                speak('Sorry Sir! I am unable to send your message at this moment!')

    elif 'nothing' in query or 'abort' in query or 'stop' in query:
        speak('okay')
        speak('Bye Sir, have a good day. Shutting down...')
        sys.exit()

    elif "go offline" in query:
        speak("closing all system applications. disconnecting from servers, going offline.Ggoodbye sir!")
        sys.exit()

    elif "what can you do" in query:
        return """I can send emails, report the weather forecast, open a browser and search for anything,
         I can locate places on google maps, I answer basic question, I can entertain you when you are bored,
         I can tell you the current date and time, I can open popular website at your command,
         I can take screenshots, I can find people, I do open local applications, increase and decrease volume,
         play, pause, play next song, play previous songs, play a random song or a particular song at your command, play a video"""

    elif 'hello' in query:
        return 'Hello Sir, hope you are fine'

    elif "What is the weather like" in query:
        driver = webdriver.Chrome()
        driver.get("https://www.weather-forecast.com/accra/forecasts/latest")
        t = driver.find_elements_by_class_name("b-forecast__table-description-content")[0].text
        return t

    elif "date" in query:
        return getdate()

    elif "open camtasia" in query:
        os.startfile(r"C:\Program Files\TechSmith\Camtasia 2019\CamtasiaStudio.exe")
        return "Opening camtasia..."

    elif "open corel draw" in query:
        os.startfile(r"c:\Program Files\Corel\CorelDRAW Graphics Suite X8\Programs64\\")
        return "Opening Corel Draw 2019..."

    elif "open Pycharm" in query:
        os.startfile(r"C:\Program Files\JetBrains\PyCharm Community Edition 2019.2.2\\bin\pycharm64.exe")
        speak("Opening JetBrains PyCharm Community Edition 2019...")

    elif "open file manager" in query:
        os.startfile(r"C:\Users\Stephen Dapaah\AppData\Roaming\Microsoft\Windows\Libraries")
        return "opening file manager..."

    elif "open firefox" in query:
        os.startfile(r"C:\Users\Stephen Dapaah\AppData\Roaming\Microsoft\Windows\Libraries")
        return "Opening Mozilla Fire Fox..."

    elif 'bye' in query:
        speak('Bye Sir, Have a good day. Shutting down...')
        sys.exit()

    elif "pause music" in query or "pause song" in query:
        pyautogui.press("playpause")
        return "music paused"

    elif "play song" in query:
        pyautogui.press("playpause")
        return "Playing..."

    elif "next song" in query or "next music" in query:
        pyautogui.press("nexttrack")
        return "Okay, Enjoy!"

    elif "previous song" in query or "previous music" in query:
        pyautogui.press("prevtrack")
        return "Okay, Enjoy!"

    elif "turn up volume" in query:
        q = 1
        while q <= 10:
            pyautogui.press("volumeup")
            q += 1
        return "volume increased by 20%"

    elif "turn down volume" in query:
        q = 1
        while q <= 8:
            pyautogui.press("volumedown")
            q += 1
        return "volume decreased by 20%"

    elif "play music" in query:
        speak("which song do you want me to play?")
        try:
            music = myCommand()
            path = r"E:\music\format\\"
            files = os.listdir(path)
            for file in files:
                s = file.replace("_", " ")
                r = s.replace("-", " ")
                list1 = []
                if music in r:
                    list1.append(r)
                    curr = list1[0]
                    now = curr.replace(" ", "-")
                    p = path + "{}".format(now)
                    try:
                        os.startfile(p)
                    except FileNotFoundError as e:
                        speak("couldn't find the particular song, playing similar song")
        except OSError as e:
            speak("{}".format(e) + ". Please type in the title of the song")
            music = str(input('Command: '))
            path = r"E:\music\format\\"
            files = os.listdir(path)
            # num = "A God Like You"
            for file in files:
                s = file.replace("_", " ")
                r = s.replace("-", " ")
                list1 = []
                if music in r:
                    list1.append(r)
                    #print(list1)
                    curr = list1[0]
                    print(curr)
                    now = curr.replace(" ", "-")
                    print(now)
                    p = path + "{}".format(now)
                    print(p)
                    try:
                        os.startfile(p)
                    except FileNotFoundError as e:
                        speak("couldn't find the particular song, playing similar song")

    elif 'play me a song' in query:
        music_folder = r"E:\music\format\\"
        song = os.listdir(music_folder)
        random_music = music_folder + random.choice(song)
        try:
            s = random_music.replace(" ", "")
            #print("Playing now: {}".format(random_music))
            now = random_music.split("\\")
            current = now[-1].split(".")
            final = current[-2]
            #print("final:", final)
            neat = final.replace("_", " ")
            good = neat.replace("-", " ")
            feat = good.replace("ft", "featuring")
            f = feat.replace("feat", "featuring")
            prod = f.replace("Prod", "Produced")
            speak("Now playing: {}".format(prod))
            time.sleep(0.5)
            os.system(s)
        except Exception as e:
            print("couldn't play the song: {}".format(e))

        speak('Okay, here is your music! Enjoy!')
    elif "open a website" in query:
        speak("what is the site")
        try:
            site = myCommand()
            webbrowser.get().open("www.{}".format(site))
        except OSError as e:
            speak("{}".format(e) + ". Please type in the site")
            site = str(input('Command: '))
            webbrowser.get().open("www.{}".format(site))

    elif "play video" in query:
        video_path = r"E:\movie\\"
        video = os.listdir(video_path)
        random_video = video_path + random.choice(video)

        try:
            print(random_video)
            os.startfile(random_video)
        except:
            return "Can't play video at the moment"

        return 'Okay, here is your video! Enjoy!'

    else:
        query = query
        speak('Searching...')
        try:
            try:
                res = client.query(query)
                results = next(res.results).text
                speak('WOLFRAM-ALPHA says - ')
                speak('Got it.')
                return results

            except:
                results = wikipedia.summary(query, sentences=3)
                speak('Got it.')
                speak('WIKIPEDIA says - ')
                return results

        except:
            try:
                # webbrowser.open('www.google.com')
                driver = webdriver.Chrome()
                driver.get("https://www.google.com")
                search = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
                search.send_keys(query)
                search.submit()
            except:
                return "You are offline! Please connect to the internet and try again"

    return 'Next Command!'

