from selenium import webdriver
from time import sleep, perf_counter
from pyautogui import moveTo, moveRel, press, mouseInfo, click
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Firefox()
# driver.get("http://somedomain/url_that_delays_loading")
import getpass
#username = input("Enter your username or email\n>>")
start = perf_counter()
username = "0245544577"
password = "0553533714"
#print("please enter your password:")
#password = getpass.getpass(prompt="enter your password", stream=None)
# password = input("Enter your password\n>>")

driver = webdriver.Chrome(r"E:\Compressed\chromedriver.exe")
driver.get("https://www.facebook.com/")
name = driver.find_element_by_id("email")
name.send_keys(username)
pass1 = driver.find_element_by_id("pass")
pass1.send_keys(password)
login = driver.find_element_by_id("u_0_b")
login.click()
sleep(7)




findfriends = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "fbRequestsJewel")))
findfriends.click()



# findfriends = driver.find_element_by_id("findFriendsNav")
# findfriends.click()
# findfriends = driver.find_element_by_id("fbRequestsJewel")
# findfriends.click()
viewall = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "seeMore")))
viewall.click()
# viewall = driver.find_element_by_class_name("seeMore")
# viewall.click()
sleep(3)
#mouseInfo()


def down3():
    for i in range(1, 4):
        press("down")


def down12():
    for l in range(1, 13):
        press("down")


down3()
k = 0
while k < 40:
    moveTo(588, 257)
    click()
    for i in range(1, 5):
        moveRel(0, 95, 0.2)
        sleep(0.1)
        click()
    down12()
    k += 1

tot = k * 5
print("{} friend's request sent".format(tot))
finish = perf_counter()
tm = finish - start
print("Program finished in {} seconds".format(tm))