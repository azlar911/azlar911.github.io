a = int(input("number: "))
dot = list()

for y in range(0, 2*a+2):
    for x in range(0, 2*a+2):
        if ((x-a)**2 + (y-a)**2 > a**2):
            print(" ", end="")
        else:
            print("*", end="")
    print("")