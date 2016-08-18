with open("grades.txt", "r") as f:
    cont = f.read().split("\n")
    count = len(cont)

while True:
    a = input("---------\noptions:\n1 to insert grades\n2 to print all records\n3 to print current grades average\n4 to quit\n---------\n")
    a = int(a)
    if a == 1:
        inp = int(input("Grades: "))
        with open("grades.txt", "a") as f:
            f.write("\n{0}: {1}".format(count+1, inp))
        count += 1
        print("Insert successfully!\n")
        continue
    elif a == 2:
        with open("grades.txt", "r") as f:
            cont = f.read()
            print(cont)
        continue
    elif a == 3:
        with open("grades.txt", "r") as f:
            cont = f.read().split("\n")
            total = 0
            c = 0
            for rec in cont:
                rec1 = rec.split(" ")
                total += int(rec1[1])
                c += 1
        print("Average: {0}\n".format(round(total / c, 3)))

    elif a == 4:
        break
    else:
        print("Options only within 1 - 4")