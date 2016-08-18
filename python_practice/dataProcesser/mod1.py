def md1(ilist):
    for i in ilist:
        if not isinstance(i, int):
            print("There is a instance not an integer")
            return

    print("Sum: {0}".format(sum(ilist)))

    
    ilist.sort()
    if len(ilist)%2 != 0:
        a = ilist[int((len(ilist)+1)/2)]
    else:
        a = ilist[int(len(ilist)/2)-1]+ilist[int(len(ilist)/2)]
        a /= 2
    print("Median: {0}".format(a))

    ilist.sort()
    print("Sort: " + str(ilist))
    ilist.sort(reverse = True)
    print("Reverse: " + str(ilist))

    ilist.sort()

    a = list()
    for i in ilist:
        flag = 1
        for j in range(2, i):
            if i % j == 0:
                flag = 0
                break
        if flag == 1:
            a.append(i)
    print("Primes in list: {0}".format(a))

if __name__ == "__main__":
    print("Error")