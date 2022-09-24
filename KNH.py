import random
rock="Rock"
paper="Paper"
scissors="Scissors"
points_comp=points_player=0
while True:
    player_move=input("Choose [r]ock, [p]aper or [s]cissors: ")
    if player_move=="stop":
        break
    if player_move=="r":
        player_move=rock
    elif player_move=="p":
        player_move=paper
    elif player_move=="s":
        player_move=scissors
    elif player_move=="score":
        print(f"You {points_player} : {points_comp} Computer")
        continue
    else:
        print("Invalid input. Try again. ")
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
                print("You win!")
                print("Type \"stop\" to quit.")
                print("Type \"score\" to see the score.")
    elif player_move==computer_move:
        print("Draw!")
    else:
        points_comp+=1
        print("You lose!")
        print("Type \"stop\" to quit.")
        print("Type \"score\" to see the score.")
print("Total score:")
print(f"You {points_player} : {points_comp} Computer")
if points_player>points_comp:
    print("You are the champion!")
elif points_player<points_comp:
    print("The Computer has defeated you!")
else:
    print("It's a Draw!")