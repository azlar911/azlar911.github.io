while True:
    n = int(input("number:(-1 to quit): "))
    c = 1
    m = 1
    if n == -1:
        break
    while True:
        if m % n == 0:
            print(c)
            break
        else:
            m = m * 10 + 1
            c += 1