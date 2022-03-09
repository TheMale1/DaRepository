import random
number = random.randint(1, 100)
count = 0
mode = ""
while mode != "E" and mode != "H":
    mode = input("Which mode do you want: E for easy or H for hard: ").upper()
    if mode == "E":
        max_guesses = 10
    else:
        max_guesses = 4
guess = int(input("Guess a number: "))
while guess != number and count < max_guesses:
    count += 1
    if guess > number:
        print("Too High")
    if guess < number:
         print("Too low")
    guess = int(input("Try again: "))
print("Your got it")
if guess == number:
    print(f"You got it in {count} guesses")
else:
    print("You couldn't get it in 10 guesses")

