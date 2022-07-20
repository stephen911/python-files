try:
    import tkinter as tk
    import pyautogui
    import time
except ImportError:
    import tkinter as tk
    import pyautogui
    import time


root = tk.Tk(screenName=None, baseName=None, className=" Stedap Search", useTk=1)
root.iconbitmap("search.ico")
canvas = tk.Canvas(root, height=300, width=300)
canvas.pack()


background_image = tk.PhotoImage(file="stedap_logo1.png")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg="blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry = tk.Entry(frame, font="calibra 10", xscrollcommand=True)
entry.bind("<Return>", (lambda event: search(entry.get())))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Search",
                   font="calibra 12 bold",
                   activebackground="yellow",
                   activeforeground="green",
                   relief="raised", bg="yellow",
                   command=lambda: search(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)


def search(search1):
    pyautogui.moveTo(71, 742)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.typewrite(search1)
    time.sleep(1)
    pyautogui.press("enter")
    #lower_frame['text'] = entry.get()

#lower_frame = tk.Frame(root, bg="blue", bd=10)
#lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

#label = tk.Label(root, text="Enter your search here", bg="yellow")
#label.place(relx=0.125, rely=0.004, relwidth=0.5, relheight=0.1)
root.mainloop()
