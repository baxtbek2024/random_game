import random
num = random.randint(1, 100)
while True:
    guess = int(input("Guess: "))
    if guess > num:
        print("Too big")
    elif guess < num:
        print("Too small")
    else:
        print("Correct!")
        break
