from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

name = input("Enter the chat's name")
time.sleep(5)
person = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
person.click()
textbox = driver.find_element_by_class_name("_1Plpp")
count = 1
while count <= 3:
    textbox.send_keys("Why is the  group soo quiet.")
    button = driver.find_element_by_class_name("_35EW6")
    button.click()
    count += 1


