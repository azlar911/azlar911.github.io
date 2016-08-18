import random
ans = random.randint(0,10)

def guessN(num):
	if(num == ans):
		print("You win!")
		return 1
	else:
		print("Guess again!")
		return 0

while True:
	guess = input("Please enter a number between 0 to 10: ")
	guess = int(guess)

	if guessN(guess):
		break