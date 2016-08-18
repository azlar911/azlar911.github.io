import csv

def md3():
    dic = dict()
    while True:
        aa = input("Options:\n1 to insert\n2 to del\nOthers to quit\n")
        if aa == "1":
            a = input("Insert \"Id Grade\": ")
            l = a.split(" ")
            dic[l[0]] = l[1]
            continue
        elif aa == "2":
            a = input("Insert Id to del: ")
            del dic[a]
            continue
        else:
            print(dic)

            with open("data.csv", "w") as f:
                print(type(f))
                w = csv.DictWriter(f, fieldnames=["Id", "Grade"])
                w.writeheader()
                for key,value in dic.items():
                    w.writerow({"Id": key, "Grade": value})
            break