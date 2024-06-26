print("Welcome to my computer quiz!\n")

playing = input("DO you want to play? ")

if playing != "yes":
    quit()

print("Okay! Let's play\n")

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct")
else:
    print('Incorrect!')

answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print("Correct")
else:
    print('Incorrect!')

answer = input("Which computer program converts assembly language to machine language? ")
if answer == "assembler":
    print("Correct")
else:
    print('Incorrect!')

answer = input("Which company first developed the Java programming language? ")
if answer == "sun microsystems":
    print("Correct")
else:
    print('Incorrect!')