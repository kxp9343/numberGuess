import random

while True:
	print("Welome to Number Guesser.")
	print("Press 1 to play and 2 to quit")  
	choice = input("What would you like to do") #input to see if quit
	if choice == "2":
		break
	elif choice == "1":
		minimum = int(input("What's the miminum value"))
		maximum = int(input("What's the maxinum value"))
		r = random.randint(minimum, maximum) #generates a random number
		while True: #start quessing the number
			userChoice = int(input("Guess a number: "))
			if userChoice == r:
				print("Yay! You gussed it!")
				break
			elif userChoice < r:
				print("Too low")
			elif userChoice > r:
				print("too high")
			else:
				print("Not an option")

		else:
			print("not an option, silly")





















































































