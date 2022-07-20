from bs4 import BeautifulSoup
import csv
import requests
#res = requests.get("file:///C:/Users/Stephen%20Dapaah/Documents/long.html")
url = open("long.html", "rb")
url = url.read()
soup = BeautifulSoup(url, "html.parser")
#print(soup.prettify())
csv_file = open("web.csv", "w")
csv_writer = csv.writer(csv_file)

csv_writer.writerow(["Title", "Video Source"])

# for tags in soup:
#     iframe = soup.find("iframe")
#     print(iframe)
#     print()
    # iframe = iframe.split("/")
    # source = iframe[-1]
    # title = soup.find("iframe")["title"]
    # csv_writer.writerow([title, source])
    # print("{} \t {}".format(title, source))
#print(soup.prettify())
g = soup.find_all("div")


#print(g)
count = 0
for i in g:
    u = soup.find("iframe")
    print(u)
    count += 1

print(count)

#find = soup.find_all("h2")#class_="pop_out_box is-full_width")
#para = soup.find_all("p")
#div = soup.find_all("div", class_="pop_out_box is-full_width")
# iframe = soup.find_all("article")
# for i in iframe:
#     n = iframe.find("iframe")["src"]
#     print(n)
#     print(i.prettify())
#     print()
# """
# print(iframe)
# iframe = soup.find("iframe")["src"]
# title = soup.find("iframe")["title"]
# print(title)

# print(iframe)
# iframe = iframe.split("/")
# print(iframe)
# print(iframe[-1])





#print(iframe)
#for i in iframe:
 #   print(i)
  #  print()

"""
for d in div:
    print(d.text)
print(para)

for p in para:
    print(p.text)
#print(find)
for f in find:
    print(f.text)
"""