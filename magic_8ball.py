import random

name = input("What is your name: ")
question = input("What is your question: ")

try:
    if name.strip() == "" or question.strip() == "":
        print("Make sure you enter your name and provide a question.")
    else:
        # Choosing a random number between 1-9
        random_number = random.randint(1, 9)

        # Define the possible answers based on the random number
        if random_number == 1:
            answer = "Yes - Definitely"
        elif random_number == 2:
            answer = "It is decidedly so"
        elif random_number == 3:
            answer = "Without a doubt"
        elif random_number == 4:
            answer = "Reply hazy, try again"
        elif random_number == 5:
            answer = "Ask again later"
        elif random_number == 6:
            answer = "Better not tell you now"
        elif random_number == 7:
            answer = "My sources say no"
        elif random_number == 8:
            answer = "Outlook not so good"
        else:
            answer = "Very doubtful"

        # Print the result
        print(f"{name} asks: {question}\n")
        print(f"Magic 8-ball answers: {answer}")

except:
    print("Reached end of input unexpectedly")
