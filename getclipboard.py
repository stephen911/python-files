import win32clipboard
import time
while True:
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    with open("clip.txt", "a+") as f:
        f.write(data+"\n")
        
    time.sleep(10)