name = input("What is your name?: ")
print("Welcome", name, " to this adventure!")

answer = input("You are on a dirt road, it has come to and end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk ans swim to swim across: ").lower()

    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")

    else:
        print("Not a valid option. You lose")

elif answer == "right":
    answer = input("You can to a bridge, it looks wobbly, do you want to cross it or head back ")

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? Yes or No ").lower()

        if answer == "yes":
            print("You talked to a stranger the stranger helped you crossed the bridge.")

        elif answer == "no":
            print("You ignored the stranger, you walked into a trap and lose.")

        else:
            print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")

print("Thank you for playing", name)