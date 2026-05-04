from random import randint


def randomNum(A, B):
    if A<B:
        print("A should be bigger, my guy! Try again.")
        A = int(input("Enter your upper limit, A: "))
        B = int(input("Enter your lower limit, B: "))
        return randomNum(A, B)
    elif A-B <= 2:
        print("Come on... that's too easy, let A and B be farther apart! Try again!")
        A = int(input("Enter your upper limit, A: "))
        B = int(input("Enter your lower limit, B: "))
        return randomNum(A, B)
    return randint(B, A)


def runGame(num, answer):
    if num>answer and abs(num-answer)>3:
        return "too high!"
    elif (num>answer or num<answer) and abs(num-answer)<=3:
        return "almost!"
    elif num<answer and abs(num-answer)>3:
        return "too low!"
    else:
        return "spot on!"


A = int(input("Enter your upper limit, A: "))
B = int(input("Enter your lower limit, B: "))

answer = randomNum(A, B)
tries = 5

guess = int(input(f"Now guess a random number between {A} and {B} (maximum {tries} tries): "))
while guess != answer and tries > 0:
    if guess not in range(B, A+1):
        print("Out of range")
    else:
        print(runGame(guess, answer))
        if runGame(guess, answer) == "spot on!":
            tries = 0
        else:
            if tries > 1:
                guess = int(input(f"{tries} more tries, go again: "))
            else:
                guess = int(input(f"{tries} more try, last chance: "))
    tries -= 1

if guess == answer:
    print("Hoorayyyyy!, you got it right.")
else:
    print(f"Ouuuf, tough break. The answer was actually {answer}")