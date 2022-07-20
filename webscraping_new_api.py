from bs4 import BeautifulSoup
import json
import re
import pyautogui as py
import csv
import requests
#res = requests.get("file:///C:/Users/Stephen%20Dapaah/Documents/long.html")
# html = '''
# <script type="application/json" data-initial-state="review-filter">
# {"languages":[{"isoCode":"all","displayName":"Toutes les langues","reviewCount":"573"},{"isoCode":"fr","displayName":"français","reviewCount":"567"},{"isoCode":"en","displayName":"English","reviewCount":"6"}],"selectedLanguages":["all"],"selectedStars":null,"selectedLocationId":null}
# </script>
# '''
#
# soup = BeautifulSoup(html, 'html.parser')
# res = soup.find('script')
# json_object = json.loads(res.contents[0])
#
# for language in json_object['languages']:
#     print('{}: {}'.format(language['displayName'], language['reviewCount']))
url = open("Avocado pasta recipe - BBC Food.html", "rb")
url = url.read()
soup = BeautifulSoup(url, "html.parser")
# res = soup.find('script')
res = soup.find("script", {"type" : "application/ld+json"})
json_object = json.loads(res.contents[0])
print(res)
for recipe_instruction in json_object['recipeInstructions']:
    # print('{}: {}'.format(language['displayName'], language['reviewCount']))
    print("recipe Instruction: {}".format(recipe_instruction))

prep = []
time = ""
for preptime in json_object['prepTime']:
    # print('{}: {}'.format(language['displayName'], language['reviewCount']))
    prep.append(preptime)

time = "".join(prep)
time = int(time[2:-1])


cook = []
for cooktime in json_object['cookTime']:
    # print('{}: {}'.format(language['displayName'], language['reviewCount']))
    cook.append(cooktime)
cookt = "".join(cook)
cookt = int(cookt[2:-1])

total_time = cookt + time
print("The total time for the recipe is {}".format(total_time))

name_arr = []
for name in json_object['name']:
    name_arr.append(name)


name = "".join(name_arr)
print("Name: {}".format(name))


url_arr = []
for url in json_object['image']:
    url_arr.append(url)


url = "".join(url_arr)
print("URL: {}".format(url))


for aggregate_rating in json_object['aggregateRating']:
    print("{}".format(aggregate_rating))


recipe_category_arr = []
for recipe_category in json_object['recipeCategory']:
    recipe_category_arr.append(recipe_category)


recipe_category = "".join(recipe_category_arr)
print("Recipe category: {}".format(recipe_category))


rec_cuisine_arr = []
for rec_cuisine in json_object['image']:
    rec_cuisine_arr.append(rec_cuisine)


rec_cuisine = "".join(rec_cuisine_arr)
print("Recipe cuisine: {}".format(rec_cuisine))

print("Recipe Ingredients")
for recipe_ingredients in json_object['recipeIngredient']:
    # print('{}: {}'.format(language['displayName'], language['reviewCount']))

    print("{}".format(recipe_ingredients))


print("Suitable for Diet")
for suitable_for_diet in json_object['suitableForDiet']:
    # print('{}: {}'.format(language['displayName'], language['reviewCount']))

    print("{}".format(suitable_for_diet))
# json_object = json.loads(res.contents[0])


subtree = soup.find_all(text=re.compile(r'window\.__reactInitialState__ = ({.*});'))
#it mean we are finding all text after "window.__reactInitialState__ ="

# print(subtree[0].strip().split(" "))
right_hand = subtree[0].strip()
# print(right_hand)

right_hand = right_hand.replace("window.__reactInitialState__ = ", "")
right_hand = right_hand.replace(";", "")
print(right_hand)



# final = []
# for i in right_hand:
#
#     if i == "window.__reactInitialState__" or i == "=":
#         pass
#     else:
#         final.append(i)
#
# # print(final)
# json_string = json.dumps(final)
#
try:


    string = json.loads(right_hand)
    print(type(string))
    # for key, value in string:
    #     print(key)

except Exception as e:
    print(e)





# for key in string:
#     print(key)
#
# for k in final:
#     if "stagesWithoutLinks" in k:
#         print(k)


for key, value in string.items():
    # print(" {}".format(key))
    # if "stagesWithoutLinks" in value:
    print("{} ".format(value))






#print(soup.prettify())
# mydiv = soup.find_all("div", {"class", "name f3"} )
# print(mydiv)
# country_name = []
# country_abbreviation = []
# for tags in soup.find_all("div", {"class", "name f3"} ):
#     country_name.append(tags.text.strip())
#     # print(tags.text.strip())
# for tag in soup.find_all("kbd"):
#     country_abbreviation.append(tag.text)
#     # print(tag.text)
# print(country_name)
# print(country_abbreviation)
# # print(len(country_name))
# i = 0
# py.sleep(5)
# while i < 53:
#     py.typewrite(country_abbreviation[i], interval=0.1)
#     py.press("down")
#     py.press("left")
#     py.press("left")
#     py.typewrite(country_name[i], interval=0.1)
#     py.press("end")
#     py.press("down")
#     py.press("left")
#     py.press("left")
#     py.press("left")
#
#     i += 1
#



#print(soup.prettify())
# csv_file = open("web.csv", "w")
# csv_writer = csv.writer(csv_file)
#
# csv_writer.writerow(["Title", "Video Source"])

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
# g = soup.find_all("div")
#
#
# #print(g)
# count = 0
# for i in g:
#     u = soup.find("iframe")
#     print(u)
#     count += 1
#
# print(count)
#
# #find = soup.find_all("h2")#class_="pop_out_box is-full_width")
# #para = soup.find_all("p")
# #div = soup.find_all("div", class_="pop_out_box is-full_width")
# # iframe = soup.find_all("article")
# # for i in iframe:
# #     n = iframe.find("iframe")["src"]
# #     print(n)
# #     print(i.prettify())
# #     print()
# # """
# # print(iframe)
# # iframe = soup.find("iframe")["src"]
# # title = soup.find("iframe")["title"]
# # print(title)
#
# # print(iframe)
# # iframe = iframe.split("/")
# # print(iframe)
# # print(iframe[-1])
#
#
#
#
#
# #print(iframe)
# #for i in iframe:
#  #   print(i)
#   #  print()

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


