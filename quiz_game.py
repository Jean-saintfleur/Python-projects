print("Welcome to my computer quiz!\n")

playing = input("DO you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play\n")
score = 0

answer = input("What does CPU stand for?: ")
if answer.lower() == "central processing unit":
    print("Correct")
    score +=1
else:
    print('Incorrect!')

answer = input("What does RAM stand for?: ")
if answer.lower() == "random access memory":
    print("Correct")
    score +=1
else:
    print('Incorrect!')

answer = input("Which computer program converts assembly language to machine language?: ")
if answer.lower() == "assembler":
    print("Correct")
    score +=1
else:
    print('Incorrect!')

answer = input("Which company first developed the Java programming language?: ")
if answer.lower() == "sun microsystems":
    print("Correct")
    score +=1
else:
    print('Incorrect!')

print(f"you got {score} questions correct! You got a score of {(score/4) * 100} %")