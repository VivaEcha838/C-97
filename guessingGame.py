import random
chances = 0

notChances = 0

number = random.randint(1,9)

notChances=notChances +1

while chances < 5: 
    guess = input("Enter your guess")
    notChances=notChances +1
    
    if guess == number:
        print("Congrats! You WIN")
        break
    if notChances < 5:
        print("Sorry, you lose. The number is: ", number)