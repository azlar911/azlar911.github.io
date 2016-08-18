def md2(num1):
    
    num = num1
    print("{0}'s Prime factories: ".format(num))
    for i in range(2, num+1):
        count = 0
        while True:
            if num % i == 0:
                count += 1
                num /= i
            else:
                if count != 0:
                    print("{0}^{1} ".format(i, count), end="")
                break

    print()
    num = num1
    print("{0} In binary: ".format(num))
    a = 0
    m = 1
    while num > 0:
        a += m * (num % 2)
        num //= 2
        m *= 10
    print(a)

if __name__ == "__main__":
    print("Error")