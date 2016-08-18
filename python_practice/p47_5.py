count = 0
for i in range(101, 201):
	pri = 0
	if i % 2 != 0:
		j = 3
		pri = 1
		while j*j <= i:
			if i % j == 0:
				pri = 0
				break
			j += 2
	if pri == 1:
		count += 1
		print(i)
print(count)