#pogi ng gumawa nito sesh
import random
def guess_number():
    print("Welcome to the Number Guessing Game!")
    print("1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)")
    while True:
        level = input("Please select the difficulty level:")
        if level == "1":
            chance = 10
            print(f'You have {chance} chances')
        elif level == "2":
            chance = 5
            print(f"You have {chance} chances")
        elif level == "3":
            chance = 3
            print(f"You have {chance} chances")
        else:
            print("Invalid")
            continue
        attempt = 0
        guess = None
        guess_the_number = random.randint(1, 100)
        print("I'm thinking of a number between 1 and 100.")

        while guess != guess_the_number and chance != 0:
                guess = int(input("Enter your guess: "))
                chance -= 1
                attempt += 1
                if guess > guess_the_number:
                    print(f"incorrect the number is lower than {guess}\nYou have {chance} chance left")
                elif guess < guess_the_number:
                    print(f"incorrect the number is higher than {guess}\nYou have {chance} chance left")
                elif guess == guess_the_number:
                    print(f"Congratulations !  You guessed the correct number with {attempt} attempt")
        if chance == 0:
            print(f'Game over the number was {guess_the_number}')
        play_again = input("Play again Yes or No: ")
        if play_again.lower() != "Yes":
            break
guess_number()