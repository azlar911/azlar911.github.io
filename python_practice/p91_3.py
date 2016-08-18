def fibonacci(num):
    if num == 1:
        return 1
    elif num == 0:
        return 0
    else:
        return fibonacci(num-2) + fibonacci(num-1)

a = int(input("number: "))
print(fibonacci(a-1))