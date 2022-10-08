import random

print("Enter your move: r for rock, p for paper, s for scissors")
player_choice = input(' ').lower()


valid_hand = ["r", "p", "s"]
computer_choice = random.choice(valid_hand)

print("Player: %s, Computer: %s " % (player_choice, computer_choice))

if player_choice == computer_choice:
    print("It's a tie! Try again? (y/n)")
elif player_choice == "r":
    if computer_choice == "s":
        print("Rock smashes scissors. Player wins!")
    else:
        print("Paper covers rock. Player loses!")
elif player_choice == "p":
    if computer_choice == 'r':
        print("Paper covers rock. Player wins!")
    else:
        print("Scissors cuts paper. Player loses!")
elif player_choice == "s":
    if computer_choice == "p":
        print("Scissors cuts paper. Player wins!")
    else:
        print("Rock smashes scissors. Player loses!")


