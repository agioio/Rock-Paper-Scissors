import random
import sys

valid_moves = ["Rock","Paper","Scissors","Quit"]

#key = player_move,  value == computer_move
#1 == player win, 2 == draw, 0 == computer win
outcomes = {"Rock": {"Rock": 2,"Paper": 0, "Scissors":1},
            "Paper": {"Rock": 1, "Paper":2,"Scissors":0},
            "Scissors": {"Rock":0, "Paper": 1, "Scissors": 2}}


def get_players_move():
    print("Rock, Paper or Scissors.")
    player_choice = input("What move will you make? ")

    while player_choice.capitalize() not in valid_moves:
        print("Only pick a valid move. (Rock, Paper, Scissors)")
        player_choice = input("What move will you make? ")

    return player_choice.capitalize()


def get_computer_move():
    return random.choice(valid_moves[:-1]).capitalize()


def round_winner(player,computer,p1_score,comp_score):
    outcome = outcomes[player][computer]

    if outcome == 0:
        return p1_score,comp_score+1
    
    if outcome == 1:
        return p1_score+1,comp_score
    else:
        return p1_score,comp_score



def gameplay():
    print("Welcome to the Rock, Paper and Scissors game!")
    userplays = input("Would you like to play? ")

    if userplays.upper() == "N" or userplays.upper() == "NO":
        print("Bye")
        sys.exit(0)

    print()

    comp_score = 0
    p1_score = 0

    while comp_score != 3 and p1_score != 3:
        player_choice = get_players_move()
        computer_move = get_computer_move()

        p1_score,comp_score = round_winner(player_choice,computer_move,p1_score,comp_score)

if __name__ == "__main__":
    gameplay()