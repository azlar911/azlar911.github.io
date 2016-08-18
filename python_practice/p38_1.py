a = int(input("number: "))
for i in range(a, 0, -1):
	for j in range(1, a+1-i):
		print(" ", end="")
	for j in range(a+1-i, a+1):
		print("*", end="")
	print("")