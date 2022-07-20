read = ["stephen", "yaa", "stephen", "kofi", "stephen", "yaa", "stephen", "kofi", "stephen", "yaa", "stephen", "kofi"]
dictionary = dict()
for i in read:
    if i not in dictionary:
        dictionary[i] = 1
    else:
        dictionary[i] += 1

print(dictionary)