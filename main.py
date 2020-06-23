import random
from choice import show_choice

# blal alala
# importing a package random allowing us to randomly select the computer choice

def start_function():  # we create a function which allows us to play again
    play()  # play logic
    while input("play again? (Y/N)").upper() == "Y":
        play()


def play():  # we create function
    user_score = 0
    computer_score = 0

    rounds = 1
    while rounds != 4:
        print("___Round{}___".format(rounds))
        user = user_choice()
        computer = computer_choice()
        print(computer)
        result = compare_choice(computer, user)
        if result == "user":
            user_score += 1
        elif result == "computer":
            computer_score += 1
        else:
            print("its a draw")
        # print (compare_choice(computer,user))
        rounds += 1
        print(user_score, computer_score)
    show_result(user_score, computer_score)


def show_result(user_score, computer_score):
    if user_score > computer_score:
        print("user wins")
    elif user_score == computer_score:
        print("draw")
    else:
        print("computer wins")


def user_choice():
    user_ch = input("what is your choice? ")
    print(show_choice(user_ch))
    return (user_ch)


def computer_choice():
    computer_ch = random.choice("rsp")
    print(show_choice(computer_ch))
    return (computer_ch)


# play again?

def compare_choice(computer, user):
    result = {
        ("r", "r"): None,
        ("r", "p"): "computer",
        ("r", "s"): "user",

        ("p", "p"): None,
        ("p", "s"): "computer",
        ("p", "r"): "user",

        ("s", "s"): None,
        ("s", "r"): "computer",
        ("s", "p"): "user",

    }
    return result[computer, user]


start_function()
