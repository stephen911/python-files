import pyautogui, time, sys


def paint():
    search = "paint"
    # confirm = pyautogui.confirm(text="search for paint
    # " + search, title="Comfirm your search", buttons=["OK", "Cancel"])
    # if confirm == "OK":
    # pyautogui.moveTo(71, 742)
    # pyautogui.click()
    pyautogui.press("win")
    time.sleep(0.5)
    pyautogui.typewrite(search)
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.moveTo(65, 162, 2, pyautogui.easeInElastic)
    time.sleep(1)
    pyautogui.click()
    distance = 400
    while distance > 0:
        pyautogui.dragRel(distance, 0, duration=0.2)
        distance = distance - 5
        pyautogui.dragRel(0, distance, duration=0.2)
        pyautogui.dragRel(-distance, 0, duration=0.2)
        distance = distance - 5
        pyautogui.dragRel(0, -distance, duration=0.2)


def mouse_to_middle():
    screen_width, screen_height = pyautogui.size()
    pyautogui.moveTo(screen_width / 2, screen_height / 2)


def see_xandy_coodinate():
    print("press Ctrl + c to quit.")
    try:
        while True:
            x, y = pyautogui.position()
            positionstr = "X: " + str(x).rjust(4) + "Y: " + str(y).rjust(4)
            print(positionstr, end="")
            print("\b" * len(positionstr), end="", flush=True)
    except KeyboardInterrupt:
        print("Done\n")

def scroll():
    pyautogui.moveTo(219, 743, 1)
    pyautogui.click()
    pyautogui.moveTo(1166, 639)
    time.sleep(1)
    pyautogui.scroll(10)

def searchtool():
    search = input("Enter your search\n>>")
    #confirm = pyautogui.confirm(text="search for " + search, title="Comfirm your search", buttons=["OK", "Cancel"])
    #if confirm == "OK":
    pyautogui.moveTo(71, 742)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.typewrite(search)
    time.sleep(1)
    pyautogui.press("enter")
    #else:
        #pyautogui.alert(text="Try again later", title="Bye", button="OK")


def open_tut():
    pyautogui.moveTo(218, 747, 0.5)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(699, 291)
    pyautogui.doubleClick()
    pyautogui.moveTo(656, 402, 0.5)
    pyautogui.doubleClick()
    pyautogui.moveTo(661, 491, 0.5)
    pyautogui.rightClick()
    pyautogui.moveTo(786, 383, 0.5)
    pyautogui.click()
    pyautogui.moveTo(599, 453, 0.5)
    pyautogui.click()


def screenshot():
    name = input("Enter name of the screenshot\n>>")
    fname = "{}.png".format(name)
    time.sleep(10)
    pyautogui.screenshot(fname)
    #pyautogui.screenshot(region= (0, 0, 300, 400))
    pyautogui.moveTo(71, 742, 0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.typewrite(fname)
    time.sleep(1)
    pyautogui.press("enter")


def locate_by_pic():
    #chromepic = pyautogui.locateOnScreen("smallchrome.PNG")
    pyautogui.click("smallchrome.PNG")
    time.sleep(1)
    pyautogui.typewrite("facebook.com")
    pyautogui.press("enter")


def save_snip_to_hello():
    name_snip = input("Enter name of snip\n>>")
    fname_snip = "{}.png".format(name_snip)
    search = "snip"
    pyautogui.moveTo(71, 742)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.typewrite(search)
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(15)
    pyautogui.hotkey("ctrl", "s")
    pyautogui.typewrite(fname_snip)
    time.sleep(8)
    pyautogui.moveTo(218, 745)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.locateOnScreen("snip_desktop.PNG")
    pyautogui.click("snip_desktop.PNG")
    pyautogui.locateOnScreen("snip_search.PNG")
    pyautogui.click("snip_search.PNG")
    pyautogui.typewrite(fname_snip)
    #pyautogui.locateOnScreen("snip_max.PNG")
    #pyautogui.click("snip_max.PNG")
    pyautogui.moveTo(262, 197)
    time.sleep(2)
    pyautogui.rightClick()
    time.sleep(1)
    pyautogui.moveTo(299, 581)
    time.sleep(1)
    pyautogui.click()
    pyautogui.moveTo(71, 742)
    time.sleep(1)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.typewrite("Automation")
    time.sleep(0.5)
    pyautogui.moveTo(502, 503)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "v")


def check_prime():
    n = int(input("enter the number\n>>"))
    m = n/2
    i = 2
    flag = 0

    while i <= m:
        i += 1
        if n % i == 0:
            print("The number is not prime")
            flag = 1
            break

        elif flag == 0:
            print("The number is prime")
            break
        else:
            pass


def open_word():
    pyautogui.moveTo(710, 748)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(275, 156)
    pyautogui.click()
    time.sleep(2)
    pyautogui.typewrite("=rand()")
    pyautogui.press("enter")


def graph():
    x = []
    y = []
    search = "excel"
    print("*" * 80)
    print("This program takes X-values and their corresponding Y-values to draw a graph")
    print("*" * 80)
    num = int(input("How many X-value would you like to enter?\n>>"))
    for i in range(0, num):
        xvalues = input("Enter your X-Values\n>>")
        x.append(xvalues)
    print("*" * 55)
    print("Enter their corresponding Y-values in the same order")
    print("*" * 55)
    for t in range(0, num):
        yvalues = input("Enter your y-values\n>>")
        y.append(yvalues)
    time.sleep(1)
    pyautogui.press("win")
    pyautogui.moveTo(71, 742)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.typewrite(search)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(5)
    try:
        #pyautogui.locateOnScreen("snip_excel.PNG")
        #pyautogui.click("snip_excel.PNG")
        pyautogui.moveTo(271, 202)
        pyautogui.click()
    except Exception as e:
        print("Couldn't find the image: " + str(e))
    time.sleep(2.5)
    try:
        pyautogui.locateOnScreen("snip_exbox.PNG")
        pyautogui.click("snip_exbox.PNG")
    except Exception as e:
        print("Couldn't find the image: " + str(e))

    if num == 7:
        time.sleep(0.2)
        pyautogui.typewrite(x[0])
        pyautogui.press("down")
        pyautogui.typewrite(x[1])
        pyautogui.press("down")
        pyautogui.typewrite(x[2])
        pyautogui.press("down")
        pyautogui.typewrite(x[3])
        pyautogui.press("down")
        pyautogui.typewrite(x[4])
        pyautogui.press("down")
        pyautogui.typewrite(x[5])
        pyautogui.press("down")
        pyautogui.typewrite(x[6])
        pyautogui.locateOnScreen("snip_B.PNG")
        pyautogui.click("snip_B.PNG")
        pyautogui.typewrite(y[0])
        pyautogui.press("down")
        pyautogui.typewrite(y[1])
        pyautogui.press("down")
        pyautogui.typewrite(y[2])
        pyautogui.press("down")
        pyautogui.typewrite(y[3])
        pyautogui.press("down")
        pyautogui.typewrite(y[4])
        pyautogui.press("down")
        pyautogui.typewrite(x[5])
        pyautogui.press("down")
        pyautogui.typewrite(x[6])

    elif num == 6:
        time.sleep(0.2)
        pyautogui.typewrite(x[0])
        pyautogui.press("down")
        pyautogui.typewrite(x[1])
        pyautogui.press("down")
        pyautogui.typewrite(x[2])
        pyautogui.press("down")
        pyautogui.typewrite(x[3])

        pyautogui.press("down")
        pyautogui.typewrite(x[4])
        pyautogui.press("down")
        pyautogui.typewrite(x[5])
        pyautogui.locateOnScreen("snip_B.PNG")
        pyautogui.click("snip_B.PNG")
        pyautogui.typewrite(y[0])
        pyautogui.press("down")
        pyautogui.typewrite(y[1])
        pyautogui.press("down")
        pyautogui.typewrite(y[2])
        pyautogui.press("down")
        pyautogui.typewrite(y[3])
        pyautogui.press("down")
        pyautogui.typewrite(y[4])
        pyautogui.press("down")
        pyautogui.typewrite(y[5])

    elif num == 5:
        time.sleep(0.2)
        pyautogui.typewrite(x[0])
        pyautogui.press("down")
        pyautogui.typewrite(x[1])
        pyautogui.press("down")
        pyautogui.typewrite(x[2])
        pyautogui.press("down")
        pyautogui.typewrite(x[3])
        pyautogui.press("down")
        pyautogui.typewrite(x[4])
        pyautogui.locateOnScreen("snip_B.PNG")
        pyautogui.click("snip_B.PNG")
        pyautogui.typewrite(y[0])
        pyautogui.press("down")
        pyautogui.typewrite(y[1])
        pyautogui.press("down")
        pyautogui.typewrite(y[2])
        pyautogui.press("down")
        pyautogui.typewrite(y[3])
        pyautogui.press("down")
        pyautogui.typewrite(y[4])

    elif num == 4:
        time.sleep(0.2)
        pyautogui.typewrite(x[0])
        pyautogui.press("down")
        pyautogui.typewrite(x[1])
        pyautogui.press("down")
        pyautogui.typewrite(x[2])
        pyautogui.press("down")
        pyautogui.typewrite(x[3])
        pyautogui.locateOnScreen("snip_B.PNG")
        pyautogui.click("snip_B.PNG")
        pyautogui.typewrite(y[0])
        pyautogui.press("down")
        pyautogui.typewrite(y[1])
        pyautogui.press("down")
        pyautogui.typewrite(y[2])
        pyautogui.press("down")
        pyautogui.typewrite(y[3])

    elif num == 3:
        time.sleep(0.2)
        pyautogui.typewrite(x[0])
        pyautogui.press("down")
        pyautogui.typewrite(x[1])
        pyautogui.press("down")
        pyautogui.typewrite(x[2])
        pyautogui.locateOnScreen("snip_B.PNG")
        pyautogui.click("snip_B.PNG")
        pyautogui.typewrite(y[0])
        pyautogui.press("down")
        pyautogui.typewrite(y[1])
        pyautogui.press("down")
        pyautogui.typewrite(y[2])

    elif num == 2:
        time.sleep(0.2)
        pyautogui.typewrite(x[0])
        pyautogui.press("down")
        pyautogui.typewrite(x[1])
        pyautogui.locateOnScreen("snip_B.PNG")
        pyautogui.click("snip_B.PNG")
        pyautogui.typewrite(y[0])
        pyautogui.press("down")
        pyautogui.typewrite(y[1])

    elif num == 1:
        time.sleep(0.2)
        pyautogui.typewrite(x[0])
        pyautogui.locateOnScreen("snip_B.PNG")
        pyautogui.click("snip_B.PNG")
        pyautogui.typewrite(y[0])


    pyautogui.press("down")
    pyautogui.press("up")
    pyautogui.hotkey("ctrl", "a")
    time.sleep(2)
    try:
        pyautogui.locateOnScreen("snip_insert.PNG")
        pyautogui.click("snip_insert.PNG")
    except Exception as e:
        print("Couldn't find the image: " + e)
    time.sleep(3)
    try:
        pyautogui.locateOnScreen("snip_scatter.PNG")
        pyautogui.click("snip_scatter.PNG")
    except Exception as e:
        print("Couldn't find the image: " + e)
    time.sleep(3)
    pyautogui.moveRel(100, 400, duration=0.5)
    time.sleep(2)
    pyautogui.click()
    pyautogui.moveTo(430, 315)
    time.sleep(2)
    pyautogui.click()

    # pyautogui.locateOnScreen("snip_dia.PNG")
    # pyautogui.click("snip_dia.PNG")
    pyautogui.moveRel(400, 0, duration=0.5)
    pyautogui.click()
    time.sleep(1.5)
    try:
        pyautogui.locateOnScreen("snip_okay.PNG")
        pyautogui.click("snip_okay.PNG")
    except Exception as e:
        print("Couldn't find the image: " + e)
    time.sleep(2)
    try:
        pyautogui.locateOnScreen("snip_plus.PNG")
        pyautogui.click("snip_plus.PNG")
    except Exception as err:
        print("cant find trendline: {}".format(err))
    time.sleep(0.5)
    pyautogui.moveTo(997, 490)
    time.sleep(1)
    pyautogui.click()
    confirm = pyautogui.confirm("Do you want to print or save the Graph?", "Print Command", buttons=["Print", "Save", "Cancel"])
    if confirm == "Print":
        pyautogui.hotkey("ctrl", "p")
    elif confirm == "Save":
        pyautogui.hotkey("ctrl", "s")
    else:
        pass
    # pyautogui.locateOnScreen("snip_trendline.PNG")
    # pyautogui.click("snip_trendline.PNG")



# pyautogui.moveTo(100, 200, 5, pyautogui.easeInElastic)
# pyautogui.move(600, 800, 5, pyautogui.easeInCirc)
# pyautogui.click()
# pyautogui.moveTo(500, 0, 1)
# pyautogui.dragTo(200, 600, 2, button='left')
# pyautogui.dragTo(800, 400, 2, button='left')
# pyautogui.click(x=300, y=400)
# pyautogui.click(clicks=2, interval=0.5)
# pyautogui.click(button='right', clicks=3, interval=0.5)
# pyautogui.doubleClick()
# pyautogui.mouseDown()
# pyautogui.mouseUp()
# pyautogui.position()
# messages
# pyautogui.alert()
# pyautogui.confirm()
# pyautogui.password()
# pyautogui.prompt()
# pyautogui.hotkey("ctrl", "shift", "esc", "c")
# pyautogui.mouseInfo()
# pyautogui.mouseInfo()


paint()
# save_snip_to_hello()
#searchtool()
# pyautogui.mouseInfo()
# open_tut()
#screenshot()
# pyautogui.moveTo(218, 745)paint

# pyautogui.click()
# time.sleep(1)
# pyautogui.moveTo(1357, 693)
# pyautogui.scroll(10, x=1357, y=693)
# screenshot()
# pyautogui.mouseInfo()
# open_word()
#pyautogui.mouseInfo()
# print(x, y)
# graph()
#see_xandy_coodinate()