import random 

def play():
    user = input("What's your choice?: 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        return "tie"

    # if the user win
    if is_win(user, computer):
        return "You won!"

    return "You lost!"

def is_win(player, oppenent):
    # return true if player win

    if (player == "r" and oppenent == "s") or (player == "s" and oppenent == "p") or (player == "p" and oppenent == "r"):
        return True

print(play())