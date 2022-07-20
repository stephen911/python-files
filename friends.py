from selenium import webdriver
import win32api, win32con
import time
import unittest
import datetime
import type_text as keyboard
from bs4 import BeautifulSoup


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


facebook = "https://www.facebook.com/"
emails = ['youremail@gmail.com']
passwords = ['yourpassword']
friends_to_add = 5


class GetAttributeTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(facebook)
        time.sleep(3)

    def test_GetAttribute(self):
        driver = self.driver
        for index in xrange(0, len(emails)):
            print
            'User enters email "%s", password "%s" and clicks on "Login" button' % (emails[index], passwords[index])
            email = driver.find_element_by_id('email')
            email.send_keys('%s' % emails[index])
            password = driver.find_element_by_id('pass')
            password.send_keys('%s' % passwords[index])
            driver.find_element_by_id('loginbutton').click()
            time.sleep(3)
            print
            "Redirecting to profile page"
            driver.get("https://www.facebook.com/profile.php")
            time.sleep(3)
            friends_amount = int(driver.find_element_by_xpath("//span[@class='_gs6']").text)
            print
            "Current user has %s friends" % friends_amount
            driver.find_element_by_link_text("Friends").click()
            time.sleep(3)

            print
            "Choosing scroll down amount depending on current user's friends amount"
            press_down_amount = friends_amount
            for press in xrange(0, press_down_amount):
                keyboard.Press("DOWN")

            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            new_user_profiles = []
            for link in soup.findAll("a", {"class": "_39g5"}):
                new_profile = link.get('href')
                if "facebook" in new_profile:
                    new_user_profiles.append(new_profile)

            print
            "Amount of user profiles displayed: %s" % len(new_user_profiles)

            if len(new_user_profiles) > 120:
                random_number = int(datetime.datetime.now().minute) * 2
            elif len(new_user_profiles) > 180:
                random_number = int(datetime.datetime.now().minute) * 3
            elif len(new_user_profiles) > 240:
                random_number = int(datetime.datetime.now().minute) * 4
            elif len(new_user_profiles) > 300:
                random_number = int(datetime.datetime.now().minute) * 5
            elif len(new_user_profiles) > 360:
                random_number = int(datetime.datetime.now().minute) * 6
            elif len(new_user_profiles) > 420:
                random_number = int(datetime.datetime.now().minute) * 7
            elif len(new_user_profiles) > 480:
                random_number = int(datetime.datetime.now().minute) * 8
            elif len(new_user_profiles) > 540:
                random_number = int(datetime.datetime.now().minute) * 9
            elif len(new_user_profiles) > 600:
                random_number = int(datetime.datetime.now().minute) * 10
            elif len(new_user_profiles) > 660:
                random_number = int(datetime.datetime.now().minute) * 11
            else:
                random_number = int(datetime.datetime.now().minute)

            random_profile = new_user_profiles[random_number]
            print
            "Redirecting to random profile: %s" % random_profile
            driver.get(random_profile + "_suggested")
            time.sleep(3)

            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            mutual_friends = []
            for link in soup.findAll("a", {"class": "_39g5"}):
                mutual_link = link.get('href')
                if "mutual" in mutual_link:
                    mutual_friends.append(mutual_link)
            print
            "Found %s mutual friend links" % len(mutual_friends)

            if len(mutual_friends) > friends_to_add:
                try:
                    for friend_id in range(0, friends_to_add):
                        try:
                            driver.find_elements_by_css_selector(
                                "button._42ft._4jy0.FriendRequestAdd.addButton._4jy3._517h._51sy")[friend_id].click()
                            time.sleep(.7)
                        except:
                            print
                            "Couldn't find 'Add friend' button or error was displayed"
                            keyboard.Press("ENTER")
                except:
                    pass
            else:
                print
                "Amount of mutual friends was less than you wanted to add"

            driver.get(facebook)
            time.sleep(3)
            driver.find_element_by_id('pageLoginAnchor').click()
            time.sleep(3)
            driver.find_element_by_link_text('Log Out').click()
            time.sleep(3)


if __name__ == '__main__':
    unittest.main()