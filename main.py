import random


def get_choices():
    player_choice = input("Enter a choice (rock , paper , scissors : )")
    options = ["rock", "paper", "scissor"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


# def greeting():
#     return "Hi"
# response = greeting()
# print(response)
# choices = get_choices()
# print(choices)
# dict = {"name": "beau", "color": choices}
# list
# food = ["pizza", "carrots", "eggs"]
# dinner = random.choice(food)


def check_win(player, computer):
    print("You chose" + player + ", computer chose" + computer)
    if player == computer:
        return "It's a tie!"


# is
# in
# operator

print("ArPiT".lower())
