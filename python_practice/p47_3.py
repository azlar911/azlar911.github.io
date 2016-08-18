a = input("Input a date: (mm-dd)")
mon = int(a[0])*10 + int(a[1])
day = int(a[3])*10 + int(a[4])
d = 0

md = [31,28,31,30,31,30,31,31,30,31,30,31]
cmd = [0]
for i in range(1, 12):
	cmd.append(cmd[i-1] + md[i-1])

print(cmd[mon-1]+ day)