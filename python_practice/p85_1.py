a="1,62,4,23,7,5,33,4,5"
b = a.split(",")

for i in range(0, 9):
	b[i] = int(b[i])

print(b)
print(len(b))
print("Max: " + str(max(b)))
print("Min: " + str(min(b)))