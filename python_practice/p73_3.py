mon = 1
day = 1
mday = [31,28,31,30,31,30,31,31,30,31,30,31]

nday = 1
for i in range(1, 366):
    with open("p73_3/"+str(mon)+"-"+str(day)+".txt", "w") as f:
        f.write(str(nday))
    nday += 1
    day += 1
    if day > mday[mon-1]:
        day = 1
        mon += 1