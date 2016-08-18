a = int(input("Input a number: "))
b = 1
c = 0
while a != 0:
	c += (a%2) * b
	b *= 10
	a = a//2
print(c)