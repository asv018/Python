def get_choices():
    player_choice = input("Enter a choice (rock , paper , scissors : )")
    computer_choice = "paper"
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


# def greeting():
#     return "Hi"


# response = greeting()
# print(response)

choices = get_choices()
print(choices)


dict = {"name": "beau", "color": choices}
