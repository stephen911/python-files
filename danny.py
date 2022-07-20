# import PySimpleGUI as sg
# from pyautogui import confirm
# # from easygui import diropenbox
# from os import startfile
# import  webbrowser
#
# # webbrowser.open_new("cash.pdf")
# # startfile("cash.pdf")
# sg.theme("DarkTeal2")
# layout = [[sg.T("")], [sg.Text("Select a folder: "), sg.Input(key="") , sg.FolderBrowse(key="-IN-")], [sg.T("")], [sg.Button("Organise files"),]]
#
# ###Building Window
# window = sg.Window('PDF Reader', layout,icon="organiser.ico", size=(600, 300), element_justification="center")
#
#
# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED or event == "Exit":
#         break
#     elif event == "Organise files":
#         pass
#         # function call
#         # print(values["-IN-"])
import pyautogui
pyautogui.mouseInfo()



x = sub("hellhhhffggffgfm")