import random
import time

print("""
*********************************

Welcome to the Number Guessing Game ..

*********************************
""")

print("Please guess a number between 1 and 100..")

random_number = random.randint(1,100)

life=10

while True:

    guess = int(input("Please enter a number."))

    if guess < random_number:
        print("Please wait...")
        time.sleep(1)

        print("Please enter a bigger number.")
        life -=1

    elif guess > random_number:
        print("Please wait...")
        time.sleep(1)

        print("Please enter a smaller number")
        life -=1

    else:
        print("Congratulations .. You won :)) ")
        exit()

    if life ==0:
        print("Sorry, you lost :( ")
        break
