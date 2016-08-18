mday = [31,28,31,30,31,30,31,31,30,31,30,31]

def checkDate(mon, day):
    if mon > 11 or mon < 0:
        return 0
    else:
        if 0 < day <= mday[mon]:
            return 1
        return 0


while True:
    mon = int(input("Month: "))
    day = int(input("Day: "))
    if mon == -1:
        break
    if checkDate(mon-1, day):
        print("Valid")
    else:
        print("Invalid")