#Rock paper scissors game.

import random;

options=("rock", "paper", "scissors");
running=True;

player_score=0;
computer_score=0;


while running:
    computer=random.choice(options); # auto picks a random choice
    player=None;

    while player not in options: #player cannot input invalid option
        player=input("Pick an option(rock,paper/scissors):  ").lower();# prompt user to choose
    
    if player==computer:
        print(f"Player: {player}");
        print(f"Computer: {computer}");
        print(f"its a tie.");
        print("-----------------------");
        print(f"You score: {player_score}\nComputer:{computer_score}");
    elif player=='rock' and computer=='scissors':
        print(f"Player: {player}");
        print(f"Computer: {computer}");
        print("You win !");
        player_score+=1;
        print("-----------------------");
        print(f"You score: {player_score}\nComputer:{computer_score}");
    elif player=='paper' and computer=='rock':
        print(f"Player: {player}");
        print(f"Computer: {computer}");
        print(f"You win!");
        player_score+=1;
        print("-----------------------");
        print(f"You score: {player_score}\nComputer:{computer_score}");
    elif player=='scissors' and computer=='paper':
        print(f"Player: {player}");
        print(f"Computer: {computer}");
        print(f"You win!");
        player_score+=1;
        print("-----------------------");
        print(f"You score: {player_score}\nComputer:{computer_score}");
    else:
        print(f"Player: {player}");
        print(f"Computer: {computer}");
        print(f"You lose!");
        computer_score +=1;
        print("-----------------------");
        print(f"You score: {player_score}\nComputer:{computer_score}");

    if not input("Play again?(y/n): ").lower()=='y':# provide a sense of democracy
        running=False;
    
print("Thank you for playing.");

