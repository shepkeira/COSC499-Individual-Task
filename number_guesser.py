import math
#Game A
def pick_number():
    print("I am a number guesser!")
    print("Pick a number, between 100 and 0, that you want me to guess, but don't tell me yet!")
    high = 100
    low = 0
    guess = math.floor((high-low)/2 + low)
    done = False
    while not done:
        print("Is the number ", guess)
        ans = input("A - Correct!\nB - Too High\nC - Too Low\n")
        guess, done = change_guess(ans, guess, high, low)
    return guess



def change_guess(ans, guess, high, low):
    success = False
    if ans == "A":
        print("I Won!")
        success = True
    elif ans == "B":
        high = guess
        guess = math.floor((high - low)/2 + low)
    elif ans == "C":
        low = guess
        guess = math.floor((high - low)/2 + low)
    else:
        print("That wasn't an answer, please enter A, B, or C")
    return guess, success

if __name__ == "__main__":
    pick_number()