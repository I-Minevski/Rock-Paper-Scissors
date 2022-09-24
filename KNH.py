import random
import sys
from colorama import Fore, Back, Style
rock="Rock"
paper="Paper"
scissors="Scissors"
points_comp=points_player=0
while True:
    player_move=input(Fore.GREEN + "Choose [r]ock, [p]aper or [s]cissors: ")
    if player_move=="stop":
        break
    if player_move=="r":
        player_move=rock
    elif player_move=="p":
        player_move=paper
    elif player_move=="s":
        player_move=scissors
    elif player_move=="score":
        print(Fore.WHITE + f"You {points_player} : {points_comp} Computer")
        continue
    else:
        print(Fore.RED + "Invalid input. Try again. ")
        continue
    computer_random_choice=random.randint(1, 3)
    computer_move=""
    if computer_random_choice==1:
        computer_move=rock
    elif computer_random_choice==2:
        computer_move=paper
    elif computer_random_choice==3:
        computer_move=scissors
    print(f"The Computer chose {computer_move}.")
    if (player_move==rock and computer_move==scissors) or \
            (player_move==scissors and computer_move==paper) or \
                (player_move==paper and computer_move==rock):
                points_player+=1
                print(Fore.BLUE + "You win!")
                print(Fore.WHITE + "Type [stop] to quit.")
                print(Fore.WHITE + "Type [score] to see the score.")
    elif player_move==computer_move:
        print(Fore.YELLOW + "Draw!")
    else:
        points_comp+=1
        print(Fore.RED + "You lose!")
        print(Fore.WHITE + "Type [stop] to quit.")
        print(Fore.WHITE + "Type [score] to see the score.")
print(Fore.GREEN + "Total score:")
print(f"You {points_player} : {points_comp} Computer")
if points_player>points_comp:
    print(Fore.BLUE + "You are the champion!")
elif points_player<points_comp:
    print(Fore.RED + "The Computer has defeated you!")
else:
    print(Fore.YELLOW + "It's a Draw!")