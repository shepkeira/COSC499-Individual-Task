import math

def pick_number():
    print("I am a number guesser!")
    print("Pick a number, between 100 and 0, that you want me to guess, but don't tell me yet!")
    high = 100
    low = 0
    guess = math.floor((high-low)/2 + low)
    while True:
        print("Is the number ", guess)
        ans = input("A - Correct!\nB - Too High\nC - Too Low\n")
        if ans == "A":
            print("I Won!")
            break
        elif ans == "B":
            high = guess
            guess = math.floor((high - low)/2 + low)
        elif ans == "C":
            low = guess
            guess = math.floor((high - low)/2 + low)
        else:
            print("That wasn't an answer, please enter A, B, or C")

pick_number()