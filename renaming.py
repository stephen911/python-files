import os
# from winsound import Beep

# frequency = 2500
# duration =  10000
#print("\a")
#Beep(frequency, duration)
#os.path.isdir()
#os.path.isfile()
#os.path.exists()
#os.write()
path = r"C:\xampp\htdocs\naseamin"
files = os.listdir(path)
for file in files:
    #print(file)
    n = file[-5:]
    if n == ".html":
        
        m = file.replace(n, ".php")
        #n = file[-4:]
        #m = file.replace(n, ".png")
        #os.replace(r"C:\Users\Stephen Dapaah\Desktop\snip\{}".format(file), r"C:\Users\Stephen Dapaah\Desktop\snip\{}".format(m))
        os.replace(path + "\\{}".format(file), path + "\\{}".format(m))

