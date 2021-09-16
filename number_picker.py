from random import randint
import math

def guess_number():
    num = int(randint(0, 100))
    print("I am a random number generater!")
    print("But the trick is you have to guess the number I picked haha")
    print("My number is between 0 and 100")
    success = False
    while not success:
        guess = accept_guess()
        message, success = compare_number(num, guess)
        print(message)
    return guess

def accept_guess():
    success = False
    while not success:
        try:
            guess = int(input("Pick a number between 0 and 100: "))
        except ValueError:
            print("Make sure you enter only a number")    
        else:
            success = True
    return guess

def compare_number(num, guess):
    print("num: ", type(num))
    print("guess: ", type(guess))
    success = False
    if num == guess:
        message = "Correct!"
        success = True
    elif num > guess:
        message = "Too low guess again"
    else:
        message = "Too high guess again"
    return message, success

if __name__ == "__main__":
    guess_number()