#RPS.py
#Name: Michelle Diaz
#Date: 9/9/2025
#Assignment: RPS.py
import random

def main():
  wins = 0
  ties = 0
  losses = 0

  playagain = "Y"
  while playagain == "Y":
    #Create a loop that continues as long as the user wants to play.
    #User can play as many games as they wish.
    #Randomly choose the computer between 'R', 'P', or 'S'
    computer = random.choice( ["R", "P", "S"] )
    #Prompt the user for their RPS selection
    player = input("Pick your weapon (R, P, S): ")
    #Determine winner and state what happened to the user
    if computer == "R":
      print("Computer chose rock")
    elif computer == "P": 
      print("Computer chose paper")
    else:
      print("Computer chose scissors")

    if player == "R":
      print("Player chose rock")
    elif player == "P":
      print("Player chose paper")
    else:
      print("Player chose scissors")

    if player == "R" and computer == "R":
      print("Tie")
      ties= ties + 1

    if player == "R" and computer == "P":
      print("Computer Wins.")
      losses = losses + 1

    if player == "R" and computer == "S":
      print("You Win!")
      wins = wins + 1 

    if player == "P" and computer == "R":
      print("You win!")
      wins = wins + 1

    if player == "P" and computer == "P":
      print("Tie")
      ties = ties + 1

    if player == "P" and computer == "S":
      print("Computer Wins.")
      losses = losses + 1 

    if player == "S" and computer == "R":
      print("Computer wins.")
      losses = losses + 1 
    
    if player == "S" and computer == "P":
      print("You win!")
      win = win + 1 

    if player == "S" and computer == "S":
      print("Tie")
      ties = ties + 1 

    #Ask the user if they would like to play again.
    playagain = input("Play again? (Y/N)?: ")
    #In the end, print the stats
    print("Wins \t Ties \t Losses")
    print("---- \t ---- \t ------")
    print(wins, "\t", ties , "\t", losses)


if __name__ == '__main__':
  main()
