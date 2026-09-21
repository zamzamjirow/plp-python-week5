secret = 7
attempts = 0

while True:
    guess = int(input("Guess the number (1-20): "))
    attempts = attempts + 1

    if guess > secret:
        print("Too high!")
    elif guess < secret:
        print("Too low!")
    else:
        print("Correct!")
        break

print(f"You got it in {attempts} tries!")