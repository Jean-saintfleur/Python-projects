import random 

top_of_range = input("Pick a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than zero next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()
random_number = random.randint(0, top_of_range)
user_guess_count = 0

while True:
    user_guess_count += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
       print("Please type a number next time.")
       continue

    if user_guess == random_number:
        print("You guessed the correct the number!")
        break
    elif user_guess > random_number:
        print("Your guess was too high!")
    else:
        print("Your guess was too low!")

print(f"You got it in {user_guess_count}, guesses.")