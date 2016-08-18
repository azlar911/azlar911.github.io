import random
ans = random.randint(1, 100)

def guess(num):
    if num == ans:
        print("you win!")
        return 0
    elif num > ans:
        print("Less!")
        return 1
    else:
        print("Greater!")
        return 1

while True:
    a = int(input("Guess a number: "))
    if guess(a) == 0:
        break