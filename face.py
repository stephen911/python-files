
import webbrowser
import chromedriver_binary
from selenium import webdriver
from time import sleep

usr = input('Enter Email Id:')
pwd = input('Enter Password:')

driver = webdriver.Chrome("C:\\Users\\Stephen Dapaah\\source\\repos\\selenium\\packages\\Selenium.WebDriver.ChromeDriver.78.0.3904.10500\\driver\\win32\\chromedriver.exe")
driver.get('https://www.facebook.com/')
print("Opened facebook")
sleep(10)

username_box = driver.find_element_by_id('email')
username_box.send_keys(usr)
print("Email Id entered")
sleep(3)

password_box = driver.find_element_by_id('pass')
password_box.send_keys(pwd)
print("Password entered")

login_box = driver.find_element_by_id('loginbutton')
login_box.click()

print("Done")
input('Press anything to quit')
driver.quit()
print("Finished")