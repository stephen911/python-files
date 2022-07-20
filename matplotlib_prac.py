import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import csv

with open("houses_to_rent.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    lang = Counter()
    #row = next(csv_reader)
    #print(row["fire insurance"])
    for row in csv_reader:
        lang.update(row["rooms"])
#print(lang)

price = []
value = []
for item in lang:
    price.append(item[0])
    value.append(item[1])
print(lang)
plt.bar(price, value)
plt.show()
#plt.style.available
# plt.style.use("ggplot")
# x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 7, 28, 29, 30]
# y = [2400, 2500, 4500, 5600, 6700, 2300, 6700, 2300, 3400, 6700, 4500, 5600, 9000]
# z = [2400, 2500, 2700, 3600, 4000, 4200, 4100, 4500, 4900, 5400, 5700, 5600, 7000]
# # plt.plot(x, y, color="b", linestyle="--", marker=".", label="python")
# # plt.plot(x, z, color="k", linestyle="--", marker="o", label="Java")
# x_index = np.arange(len(x))
# width = 0.25
#
# plt.bar(x_index-width, y, color="b",width=width, linestyle="--", label="python")
# plt.bar(x_index, z, color="k",width=width, linestyle="--", label="Java")
# plt.title("A graph of median salaries against ages")
# plt.xlabel("Ages")
# plt.ylabel("Median Salary(USD)")
# plt.xticks(ticks=x_index, labels=x)
# plt.legend()
#
#
# #plt.tight_layout()
# plt.show()
#
