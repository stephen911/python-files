a = []
m = [1, 2, 3, 4]
flag = False

for i in range(len(m)):
	a.append(m[i])

for k in range(len(m)):

	for j in range(len(a)-1):
		if m[k] == a[j]:
			print(m[k], a[j+1])
			flag = True

if flag:
	print("there is a duplicate")
else:
	print("there is no duplicate")