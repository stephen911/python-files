from bs4 import BeautifulSoup
import requests
website = "https://www.google.com"
res = requests.get(website)
soup = BeautifulSoup(res.text, "html.parser")
link_tags = soup.find_all("a")
f = open("web.txt", "w")
for link in link_tags:
    print(link.get("href"))
    fine = str(link)
    if "https" in fine:
        print(fine)
        f.write(str(link))

f.close()


