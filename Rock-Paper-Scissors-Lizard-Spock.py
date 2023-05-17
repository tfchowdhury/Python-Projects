#Play Rock-Paper-Scissors-Lizard-Spock with Sheldon

import random

# Welcoming the player to the game

print("\nHello! I'm Dr. Sheldon Cooper and I welcome you in this fun game")
print("called Rock-Paper-Scissors-Lizard-Spock [Press Enter to Play]")
input()
print("Allow me to introduce you to the rules: \n")
print("Scissors cuts paper")
print("Paper covers rock")
print("Rock crushes lizard")
print("Lizard poisons spock")
print("Spock smashes scissors")
print("Scissors decapitates lizard")
print("Lizard eats paper")
print("Paper disproves spock")
print("Spock vaporizes rock")
print("and as it always has,")
print("Rock crushes scissors.")

    
def main():
        
    user_action = input("\nEnter a choice: ").lower()
    possible_actions = ["rock", "paper", "scissors", "lizard", "spock"]
    sheldon_action = random.choice(possible_actions)

    while user_action not in possible_actions:
        user_action = input("Invalid choice. Please choose rock, paper, scissors, lizard, or spock: ").lower()
                        
    print(f"\nYou chose {user_action}, Sheldon chose {sheldon_action}.\n")
    determine_winner(user_action, sheldon_action)
    play_again()


def determine_winner(user_action, sheldon_action):
    if user_action == sheldon_action:
        print(f"Both players selected {user_action}. It's a tie!")

# Rules for rock
        
    elif user_action == "rock":
        if sheldon_action == "paper":
            print("Paper covers rock! You lose.")
        elif sheldon_action == "scissors":
            print("Rock crushes scissors! You win!")
        elif sheldon_action == "lizard":
            print("Rock crushes lizard! You win!")
        else:
            print("Spock vaporizes rock! You lose.")

# Rules for paper
            
    elif user_action == "paper":
        if sheldon_action == "rock":
            print("Paper covers rock! You win!")
        elif sheldon_action == "scissors":
            print("Scissors cuts paper! You lose.")
        elif sheldon_action == "lizard":
            print("Lizard eats paper! You lose.")
        else:
            print("Paper disproves spock! You win!")

# Rules for scissors

    elif user_action == "scissors":
        if sheldon_action == "rock":
            print("Rock crushes scissors! You lose.")
        elif sheldon_action == "paper":
            print("Scissors cuts paper! You win!")
        elif sheldon_action == "lizard":
            print("Scissors decapitates lizard! You win!")
        else:
            print("Spock smashes scissors! You lose.")

# Rules for lizard

    elif user_action == "lizard":
        if sheldon_action == "rock":
            print("Rock crushes lizard! You lose.")
        elif sheldon_action == "paper":
            print("Lizard eats paper! You win!")
        elif sheldon_action == "scissors":
            print("Scissors decapitates lizard! You lose.")
        else:
            print("Lizard poisons spock! You win!")

# Rules for spock

    elif user_action == "spock":
        if sheldon_action == "rock":
            print("Spock vaporizes rock! You win!")
        elif sheldon_action == "paper":
            print("Paper disproves spock! You lose.")
        elif sheldon_action == "scissors":
            print("Spock smashes scissors! You win!")
        else:
            print("Lizard poisons spock! You lose.")

    else:
        print("Invalid choice!")


# Asking user if they want to play again
def play_again():
    another_game = input(f"\nDo you want to play again? (yes/no): ").lower()
    while another_game != 'yes' and another_game != 'no':
        another_game = input("Invalid choice. Do you want to play again? (yes/no): ").lower()
    if another_game == 'yes':
        main()
    else:
        print("\nSo you want to make me angry by not playing again? [Enter]")
        input()
        print("... ...")
        print("\nBazinga!")
        print("Have a wonderful day!")
        

# Calling the main function
main()
        
        
    
        
    

    
