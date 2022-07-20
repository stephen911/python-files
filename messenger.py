import pyautogui as p
import time
#p.mouseInfo()
message = """Did you know you could make money in the comfort of your home? Have you been looking for a legit online business to put a stop to all your financial crisis? Have you run out of options thinking that all is lost? Then look no further. There's an amazing offer on the table that's going to blow your mind. Hit me up now for more details"""
count = 1
while count < 4:
    p.moveTo(157, 140)


    def mess():
        p.click()
        time.sleep(2)
        p.moveTo(199, 639)
        p.click()
        time.sleep(2)
        #p.typewrite(message, 0.03)
        p.hotkey("ctrl", "v")
        p.moveTo(324, 579)
        #p.click()
        time.sleep(1)
        p.moveTo(292, 695)
        p.click()
        time.sleep(0.2)
        p.click()
        time.sleep(0.2)
        p.click()
        time.sleep(1)
    mess()
    p.moveTo(177, 216)
    mess()
    p.moveTo(190,291)
    mess()
    p.moveTo(188,360)
    mess()
    p.moveTo(202,433)
    mess()
    p.moveTo(178,498)
    mess()
    p.moveTo(180,570)
    mess()
    p.moveTo(171, 640)
    p.dragTo(157, 50, 1)
    count += 1