import webbrowser
import time
import random


while True:
    sites = random.choice(["google.com", "stedap1.site.live", "stedap.site.live", "facebook.com", "yahoo.com", "alison.com",])
    visit = "http://www.{}".format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(5, 10)
    print(seconds)