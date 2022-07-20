from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
u = input("continue")
print(u)
print("Selecting chat...")
time.sleep(5)
chat = driver.find_element_by_xpath("//*[@id=\"pane-side\"]/div[1]/div/div/div[8]/div/div/div[2]")
chat.click()
print("Selecting the typebar...")
time.sleep(5)
type = driver.find_element_by_xpath("//*[@id=\"main\"]/footer/div[1]/div[2]")
type.click()
type.send_keys("i am good")
print("Typing the messages...")
counter = 0
while counter >= 5:
    type.send_keys("hello how are you doing?")
    type.send_keys()
    counter += 1
print("Pressing the send button...")
send = driver.find_element_by_xpath("//*[@id=\"main\"]/footer/div[1]/div[3]")
send.click()

