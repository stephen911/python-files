import pysh
link = input("enter the link")
shortner = pyshorteners.Shortener()
x = shortner.tinyurl.short(link)
print
