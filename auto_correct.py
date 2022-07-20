from textblob import TextBlob
file1 = open("correct.txt", "r+")
a = file1.read()

print("original text: {}".format(str(a)))
b = TextBlob(a)
print("Corrected text: {}".format(str(b.correct())))
file1.close()
d = open("correct.txt", "w")
d.write(str(b.correct()))
d.close
