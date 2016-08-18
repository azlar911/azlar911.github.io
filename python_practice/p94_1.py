while True:
    a = input("input \"* -1\" to quit\n").split(" ")
    if a[1] == "-1":
        break
    else:
        print(2 * int(a[0]) * int(a[1]))