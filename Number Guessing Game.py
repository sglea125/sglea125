import random


def game():

    two_numbers = input("Give me two numbers  should choose a random number between, lad: ")

    numbers = two_numbers.split()

    num1 = int(numbers[0])

    num2 = int(numbers[1])

    correct = random.randint(num1, num2)

    print(f"I'm thinking of a number between {num1} and {num2} buddy, try to guess the one: ")
    guess = None

    while guess != correct:

        guess = int(input())

        if guess == correct:

            print("You got it! Well done!")
            break

        elif guess < correct:

            print("Too low lad! Try again")

        elif guess > correct:

            print("Too high there lad! Try again")


game()