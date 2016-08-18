import random
ans = random.randint(0,10)

while True:
	guess = input("Please enter a number between 0 to 10: ")
	guess = int(guess)

	if(guess == ans):
		print("You win!")
		break
	else:
		print("Guess again!")