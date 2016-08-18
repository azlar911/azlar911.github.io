a = [1, 2, 3, 4]
count = 0

for i in a:
	for j in a:
		if i != j:
			for k in a:
				if k != i and k != j:
					print(i*100 + j*10 + k)
					count += 1
print(count)