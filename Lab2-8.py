import random

square_values = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
number_of_turns = 0
no_wins = True

print("Lets play Tic-Tac-Toe!")
player_1_pick = ""
player_2_pick = ""
player_1 = input("Enter a name for player 1 and press enter, leave blank to leave as Player 1: ")
player_2 = input("Enter a name for player 2 and press enter, leave blank to leave as Player 2: ")

#sets the players name
if (player_1 == "" or player_2 == ""):
  if (player_1 == ""):
    player_1 = "Player 1"
  if (player_2 == ""):
    player_2 = "Player 2"
else:
  pass

#assigns X or O to players
if (random.randint(1,2) == 1):
  player_1_pick = input(player_1 + ", choose X or O: ").upper()
  if (player_1_pick == "X"):
    player_2_pick = "O"
  else:
    player_2_pick = "X"
else:
  player_2_pick = input(player_2 + ", choose X or O: ").upper()
  if (player_2_pick == "X"):
    player_1_pick = "O"
  else:
    player_1_pick = "X"

#makes a move
def make_a_move(player, player_pick):
  print("""
     |     |     
  {}  |  {}  |  {}
_____|_____|_____
     |     |     
  {}  |  {}  |  {}   
_____|_____|_____
     |     |     
  {}  |  {}  |  {}  
     |     |
""" .format(square_values[0], square_values[1], square_values[2], square_values[3], 
            square_values[4], square_values[5], square_values[6], square_values[7], square_values[8]))

  status = True
  while (status == True):
    choice = input(player + " pick a square(" + player_pick + "): ")
    try:
      int(choice)
      if (1 <= int(choice) <= 9):
        if (square_values[int(choice)-1] != "X" and square_values[int(choice)-1] != "O"):
          square_values.remove(choice)
          square_values.insert(int(choice)-1, player_pick)
          status = False
        else:
          print("Square already taken, select another square.")
      else:
        print("Input not an option, choose again.")
    except ValueError:
        print("Input not an option, choose again.")

status_main = True
def check_for_a_win(value1, value2, value3):
  global status_main
  global no_wins
  if (square_values[value1] == "X" and square_values[value2] == "X" and square_values[value3] == "X"):
    status_main = False
    no_wins = False
    if(player_1_pick == "X"):
      print("Player 1 won!")
    else:
      print("Player 2 won!")
  elif (square_values[value1] == "O" and square_values[value2] == "O" and square_values[value3] == "O"):
    status_main = False
    no_wins = False
    if(player_1_pick == "O"):
      print("Player 1 won!")
    else:
      print("Player 2 won!")
  else:
    pass

def func_1(player, pick):
  global number_of_turns
  global status_main
  if (no_wins == True):
    number_of_turns = number_of_turns + 1
    make_a_move(player, pick)
    check_for_a_win(0, 1, 2)
    check_for_a_win(3, 4, 5)
    check_for_a_win(6, 7, 8)
    check_for_a_win(0, 3, 6)
    check_for_a_win(1, 4, 7)
    check_for_a_win(2, 5, 8)
    check_for_a_win(0, 4, 8)
    check_for_a_win(2, 4, 6)
  if (number_of_turns == 9 and status_main == True):
    print("It's a tie :(")
    status_main = False

while (status_main == True):
  func_1(player_1, player_1_pick)
  func_1(player_2, player_2_pick)
