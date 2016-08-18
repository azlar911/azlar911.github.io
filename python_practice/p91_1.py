def sum(num):
    if num == 1:
        return 1
    else:
        return num + sum(num-1)

a = int(input("number: "))
print(sum(a))