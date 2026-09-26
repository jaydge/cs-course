secret = 7

name = input("What is your name? ")
print("Welcome", name)

guess_number = 1
correct = False



def guess_check(guess, secret):
    if guess == secret:
        print("Correct!")
        return True
    elif guess > secret:
        print("Too high.")
    else:
        print("Too low.")
    print("You were", secret - guess, "off.")
    return False

while guess_number <= 3 and not correct:
    guess = int(input("Guess "+str(guess_number) + ". Pick a number from 1 to 10: "))
    correct = guess_check(guess, secret)
    guess_number = guess_number + 1

if not correct:
    print("Out of guesses. The number was",secret)
