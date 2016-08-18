def ins(num):
    with open("atm.txt", "r") as f:
        cont = int(f.read())
    cont += num
    with open("atm.txt", "w") as f:
        f.write(str(cont))
    print("Save successfully\n")
    return 1

def que():
    with open("atm.txt", "r") as f:
        cont = int(f.read())
    print("Current: {0}\n".format(cont))
    return 1

def out(num):
    with open("atm.txt", "r") as f:
        cont = int(f.read())
    if cont >= num:
        print("Takeout successfully\n")
        cont -= num
        with open("atm.txt", "w") as f:
            f.write(str(cont))
        return 1
    else:
        print("Not enough to take out\n")

while True:
    a = int(input("--------------\nOptions:\n1 to save in\n2 to query\n3 to take out\n4 to quit\n--------------\n"))
    if a == 1:
        inp = int(input("Amount to save in: "))
        ins(inp)
    elif a == 2:
        que()
    elif a == 3:
        outp = int(input("Amount to take out: "))
        out(outp)
    elif a == 4:
        break
    else:
        print("Options within 1-4")
