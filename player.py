import os, datetime, calendar
k = os.listdir("E:\music\Music")
#print(k)
def getDate():
    now = datetime.datetime.now()
    print(now)
    my_date = datetime.datetime.today()
    print(my_date)
    weekday = calendar.day_name[my_date.weekday()]# e.g. Monday
    print(weekday)
    monthNum = now.month
    print(monthNum)
    dayNum = now.day
    print(dayNum)

    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                   'October', 'November', 'December']
    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th',
                      '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd',
                      '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']
    return 'Today is ' + weekday + ' ' + month_names[monthNum - 1] + ' the ' + ordinalNumbers[dayNum - 1] + '.'

# getDate()
#import win32com.shell.shell as shell
#import win32event

# import openpyxl
# #import pathlib
# import winshell
# from pathlib import Path
# desktop = Path(winshell.desktop())

#os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")
# os.startfile(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")
#os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk")
#os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk")
#os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Sublime Text 3.lnk")
#wb = openpyxl.load_workbook("data.csv")
# from tkinter import *
# import pygame
# import os
# window = Tk()
# window.geometry("400x150")
#
# pygame.mixer.init()
#
# n = 0
#
#
# def start_stop():
#     pass
#     # global n
#     # n = n + 1
#     # if n == 1:
#     #     song_name = songs_listbox.get()
#     #     pygame.mixer.music.load(song_name)
#     #     pygame.mixer.music.play(0)
#     #     # music started
#     # elif (n % 2) == 0:
#     #     pygame.mixer.music.pause()
#     #     # paused
#     # elif(n % 2) != 0:
#     #     pygame.mixer.music.unpause()
#
#
# l1 = Label(window, text="MUSIC PLAYER", font="times 20")
# l1.grid(row=4, column=1)
#
# b2 = Button(window, text="O", width=20, command=start_stop())
# b2.grid(row=4, column=1)
#
# songs_list = os.listdir(r"E:\music\Music")
# songs_listbox = StringVar(window)
# songs_listbox.set("select songs")
# menu = OptionMenu(window, songs_listbox, *songs_list)
# menu.grid(row=4, column=4)
#
# window.mainloop()
#
# fps = 60
# pygame.init()
# clock = pygame.time.Clock()
# movie = pygame.Movie(random_video)
# screen_size = (1920, 1080)
# screen = pygame.display.set_mode(screen_size)
# movie_screen = pygame.Surface(movie.get_size()).convert()
# movie.set_display(movie_screen)
# movie.play()
# playing = True
# while playing:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT():
#             movie.stop()
#             playing = False
#     screen.blit(movie_screen, (0, 0))
#     pygame.display.update()
#     clock.tick(fps)
#
# pygame.quit()


# window = pyglet.window.Window()
# player = pyglet.media.Player()
# source = pyglet.media.StreamingSource()
# mediaload = pyglet.media.load(random_video)
# player.queue(mediaload)
# player.play()
#
# @window.event
# def on_draw():
#     if player.source and player.source.video_format:
#         player.get_texture().blit(50, 50)
#
# pyglet.app.run()
