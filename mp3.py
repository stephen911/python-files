import os
#import kivy
dir_path = os.path.dirname(os.path.realpath(__file__))
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith(".mp3"):
            print(root + "\\" + str(file))