import os
from easygui import diropenbox
from tkinter import messagebox, Tk
root = Tk()
root.withdraw()
import shutil



# Write the name of the directory here,
# that needs to get sorted

def organise():
    path = diropenbox()
    if path == None:
        messagebox.showinfo(title="info", message="No directory selected")
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

    messagebox.showinfo(title="info", message="Your Files has been organised successfully")

