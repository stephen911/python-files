from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as py
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://alison.com/login")

email1 = "testname4321@gmail.com"
password1 = "test1234"
email = driver.find_element_by_xpath('//*[@id="login"]/div[2]/div[2]/div[2]/div/form/div[1]/input')
email.send_keys(email1)
password = driver.find_element_by_xpath('//*[@id="login"]/div[2]/div[2]/div[2]/div/form/div[2]/input')
password.send_keys(password1)
login = driver.find_element_by_xpath('//*[@id="login"]/div[2]/div[2]/div[2]/div/form/input[3]')
login.click()
search = driver.find_element_by_xpath('//*[@id="autocomplete"]')
search.send_keys("microsoft office 2010")
click_search = driver.find_element_by_xpath('//*[@id="search_icon"]')
py.press("enter")
# time.sleep(40)
# try:
#     close = driver.find_element_by_class_name("icon-cross2")
#     close.click()
# except Exception as e:
#     pass
# try:
#     msword = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, 'btn btn-blue start-button add-course-id'))
#     )
#     msword.click()
# finally:
#     pass
time.sleep(5)

try:

    msword = driver.find_element_by_xpath('//*[@id="mobile-scroll-anchor"]/li[1]/div/div[3]/a')



        # element = driver.find_element_by_id("my-id")

    actions = ActionChains(driver)
    actions.move_to_element(msword).perform()
except Exception as e:
    print(e)
time.sleep(10)
py.moveTo(265,682)
py.click()
time.sleep(2)
py.moveTo(447,601)
py.click()
time.sleep(10)


# start = driver.find_element_by_xpath('//*[@id="top_button_right"]')
# actions.move_to_element(start).perform()
# start.click()
# close = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/span')
# close.click()
# time.sleep(10)
# try:
#
#     start_topic = driver.find_element_by_xpath('//*[@id="player_button_right"]')
#     start_topic.click()
# except Exception as e:
py.moveTo(591, 640)
time.sleep(1)
py.click()





# time.sleep(5)

# while True:
#     # grab the data
#
#     # click next link
#     try:
#         element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'icon-thick-chevron-up')))
#         element.click()
#     except TimeoutError:
#
#         break


def next():

    count = 0
    while count < 10:
        py.moveTo(893, 476)
        py.click()
        time.sleep(2)
        count += 1


def start():
    count_start = 0
    while count_start < 3:
        py.moveTo(591, 640)

        py.click()
        time.sleep(2)
        count_start += 1


next()
time.sleep(10)
start()
next()
time.sleep(10)
start()
next()
time.sleep(10)
start()
next()
time.sleep(10)
start()
next()
time.sleep(10)
start()
next()
time.sleep(10)
start()
next()
time.sleep(10)
start()
next()
time.sleep(10)
start()
next()
time.sleep(10)
start()
next()
time.sleep(10)
start()
next()
time.sleep(10)
start()
next()
time.sleep(10)
start()


# except Exception as e:
#     print(e)






# name = input("Enter the chat's name")
# time.sleep(5)
# person = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
# person.click()
# textbox = driver.find_element_by_class_name("_1Plpp")
# count = 1
# while count <= 3:
#     textbox.send_keys("Why is the  group soo quiet.")
#     button = driver.find_element_by_class_name("_35EW6")
#     button.click()
#     count += 1


