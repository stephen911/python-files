import PySimpleGUI as sg
from pyautogui import confirm
import os
# from easygui import diropenbox
# from tkinter import messagebox, Tk
# root = Tk()
# root.withdraw()
import shutil

sg.theme("DarkTeal2")
layout = [[sg.T("")], [sg.Text("Select a folder: "), sg.Input(key="") , sg.FolderBrowse(key="-IN-")], [sg.T("")], [sg.Button("Organise files"),] , [sg.Button("cancel"),]]

###Building Window
window = sg.Window('Stedap Organiser', layout,icon="organiser.ico", size=(600, 300), element_justification="center")


def organise():
    path = values["-IN-"]
    print(path)
    if path == None:

        # messagebox.showinfo(title="info", message="No directory selected")
        exit(0)

    # This will create a properly organized
    # list with all the filename that is
    # there in the directory

    list_ = os.listdir(path)

    # This will go through each and every file

    for file_ in list_:

        name, ext = os.path.splitext(file_)

        # This is going to store the extension type

        ext = ext[1:]

        # This forces the next iteration,

        # if it is the directory

        if ext == '':
            continue

        # This will move the file to the directory

        # where the name 'ext' already exists

        if os.path.exists(path + '/' + ext):

            shutil.move(path + '/' + file_, path + '/' + ext + '/' + file_)

            # This will create a new directory,

        # if the directory does not already exist

        else:

            os.makedirs(path + '/' + ext)

            shutil.move(path + '/' + file_, path + '/' + ext + '/' + file_)

    # messagebox.showinfo(title="info", message="Your Files has been organised successfully")
    confirm1 = confirm("Do you want to show organised folder?", "Show folder",
                                buttons=["Yes", "No"])
    if confirm1 == "Yes":
        #pyautogui.hotkey("ctrl", "p")
        os.startfile(values["-IN-"])
    elif confirm1 == "No":
       # pyautogui.hotkey("ctrl", "s")
        pass

    #os.startfile(values["-IN-"])



while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    elif event == "Organise files":
        organise()
    elif event == "cancel":
        print("cancelling")
        # print(values["-IN-"])