a = int(input("number: "))
for i in range(1, a+1):
	for j in range(1, a+1-i):
		print(" ", end="")
	for j in range(0, i):
		print("*", end="")
	for j in range(1, i):
		print("*", end="")
	print("")