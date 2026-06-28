import random
secret = random.randint(1, 100)
while True:
    Guess = int(input("Guess a number: "))
    if Guess == secret:
        print("correct")
        break
    elif Guess < secret:
        print("too low")
    else:
        print("too high")
