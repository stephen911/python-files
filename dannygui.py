import PySimpleGUI as sg
import threading



# from easygui import diropenbox
from os import startfile
import  webbrowser
import pyttsx3, PyPDF2
import easygui,webbrowser

# webbrowser.open_new("cash.pdf")
# startfile("cash.pdf")

speaker = pyttsx3.init()


def readerPdf(path):
    # print(events)
    # print(path)
    # print(events =="Read PDF")
    # if events == "Read PDF":
    #     print("hello")
    #
    # def talk():
    #     print("hello")
    file = path
    print(file)
    # file = easygui.fileopenbox()

    webbrowser.open_new(file)
    # book = open('oop.pdf','rb')
    book = open(file, 'rb')
    reader = PyPDF2.PdfFileReader(book)
    totalPages = reader.numPages
    # print(totalPages)
    # getting a page to read fro the user
    pagenum = int(input("enter the page you want to read from : "))
    for i in range(pagenum - 1, totalPages - 1):
        page = reader.getPage(i)
        # extracting the text from that page
        text = page.extractText()
        # reading from the pdf

        voices = speaker.getProperty('voices')
        speaker.setProperty('rate', 130)
        speaker.setProperty('voices', voices[1].id)
        speaker.say(text)
        speaker.runAndWait()



        # def stop():
        #     speaker.stop()
        #
        #
        #
        # print("good")
        #
        #
        # if events == "Read PDF":
        #
        #     print("hello")
        #     talk()
        # else:
        #     stop()

        print("running..")

        # speaker.stop()


sg.theme("DarkTeal2")
layout = [[sg.T("")], [sg.Text("Select a pdf file: "), sg.Input(key="") , sg.FileBrowse(key="-IN-")], [sg.T("")], [sg.Button("Read PDF"),], [sg.Button("cancel"),]]

###Building Window
window = sg.Window(' Fausford PDF Reader', layout,icon="organiser.ico", size=(600, 300), element_justification="center")
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":

        break
    elif event == "Read PDF":
        # start = threading.Thread(target=readerPdf(values["-IN-"]), )
        # start.start()
        speak1 = threading.Thread(target=readerPdf, args=(values["-IN-"], ))
        speak1.start()
        # readerPdf()
    elif event == "cancel":
        print("cancelling")
        speaker.stop()
        print("nice")
        exit(0)


        # speaker.runAndWait()
        # stop_speaking()













    # print(values["-IN-"])