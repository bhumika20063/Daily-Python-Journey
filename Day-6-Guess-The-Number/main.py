import random
import art
print(art.logo)
is_continue = True
while is_continue:
    GUESSING = random.randint(1, 100)
    # print(GUESSING)
    print("Welcome to Number Guessing Game!")
    print("I'm thinking of a Number between 1 and 100.")
    choose = input("Choose a difficulty: Enter 'easy' or 'hard': ").lower()
    if choose == "easy":
        print("You have 10 attempts remaining to guess the number.")
        chances = 10
        for i in range(1, 11):
            guess = int(input("Make a guess: "))
            # guess = int(input("Make a guess: "))
            if guess == GUESSING:
                print(f"You got it! The answer is {GUESSING}")
                again = input("Type 'YES' to continue or 'NO' to quit:").lower()
                if again == "no":
                    is_continue = False
                break
            elif guess > GUESSING:
                print("Too high!")
                chances -= 1
                print(f"You have {chances} attempts remaining to guess the number.")
            elif guess < GUESSING:
                print("Too low!")
                chances -= 1
                print(f"You have {chances} attempts remaining to guess the number.")
            if chances == 0:
                again = input(f"You've run out of guesses. The number was {GUESSING}. Type 'YES' to continue or 'NO' to quit:")
                if again == "yes":
                    print("\n "* 100)
                elif again == "no":
                    is_continue = False
                    print("Thanks for playing! Goodbye!")

    elif choose == "hard":
        print("You have 5 attempts remaining to guess the number.")
        chances = 5
        for i in range(1,6):
            guess = int(input("Make a guess: "))
            if guess == GUESSING:
                print(f"You got it! The answer is {GUESSING}")
                again = input("Type 'YES' to continue or 'NO' to quit:").lower()
                if again == "no":
                    is_continue = False
                break
            elif guess > GUESSING:
                print("Too high!")
                chances -= 1
                print(f"You have {chances} attempts remaining to guess the number.")
            elif guess < GUESSING:
                print("Too low!")
                chances -= 1
                print(f"You have {chances} attempts remaining to guess the number.")
            if chances == 0:
                again = input(f"You've run out of guesses.The number was {GUESSING}. Type 'YES' to continue or 'NO' to quit:").lower()
                if again == "yes":
                    print(100* "\n")
                elif again == "no":
                    is_continue = False
                    print("Thanks for playing! Goodbye!")