from selenium import webdriver
driver = webdriver.Chrome()
driver.get("www.youtube.com")
search = driver.find_element_by_xpath("")
search.click()