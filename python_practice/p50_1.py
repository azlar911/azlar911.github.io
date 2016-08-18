st = input("string: ").split(" ")

c = 0
for i in range(1, len(st)):
    c += int(st[i])
avg = c / int(st[0])

co = 0
for i in range(1, len(st)):
    if int(st[i]) >= avg:
        co += 1

pe = co / int(st[0])
print(round(pe, 3))