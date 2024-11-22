import tkinter as tk
from tkinter import messagebox
import random





class GameLogic():

 def __init__(self, board_size):

     self.board_size = board_size
     self.board = [[None for _ in range(board_size)] for _ in range(board_size)]
     self.blue_score = 0
     self.red_score = 0
     self.difficult = 0




 # to make a move on the game board 

 def make_move(self, row, col, letter):
     if self.board[row][col] is None:
         self.board[row][col] = letter
         return True

     return False



# reset the game state, also clearing the board

 def reset(self, board_size):

     self.board_size = board_size
     self.board = [[None for _ in range(board_size)] for _ in range(board_size)]
     self.blue_score = 0
     self.red_score = 0

     



# checks if al the cells in the game board are filled

 def all_cells_filled(self):

     # returns TRUE if every cell is filled, FALSE if any cell is not

     return all(cell is not None for row in self.board for cell in row)

# structure for the game, initilizes setting up the board and manages everything

class SOSGame():

 def __init__(self, root = None):

     self.root = root
     self.root.title("SOS Game")
     self.root.configure(bg="white")

     self.current_player = "Blue"

     self.current_letter = tk.StringVar(value="S")
     self.current_blue_player = tk.StringVar(value="H")
     self.current_red_player = tk.StringVar(value="H")
     self.red_letter_var = tk.StringVar(value="S")
     self.mode = tk.StringVar(value="Simple")
     self.board_size = tk.IntVar(value=5)

     self.game_logic = GameLogic(self.board_size.get())




     self.create_gui()



 # the visual for the game, all the buttons, labels to make it look good

 def create_gui(self):

     title = tk.Label(self.root, text="SOS Game", font=("Helvetica", 24, "bold"), fg="black", bg="white")

     title.grid(row=0, column=0, columnspan=8, pady=20)




     mode_label = tk.Label(self.root, text="Game Mode:", font=("Helvetica", 14), fg="black", bg="white")

     mode_label.grid(row=1, column=0, padx=10)

     tk.Radiobutton(self.root, text="Simple", variable=self.mode, value="Simple", bg="white", fg="black",

                    font=("Helvetica", 12), selectcolor="lightgray").grid(row=1, column=1)

     tk.Radiobutton(self.root, text="General", variable=self.mode, value="General", bg="white", fg="black",

                    font=("Helvetica", 12), selectcolor="lightgray").grid(row=1, column=2)




     size_label = tk.Label(self.root, text="Board Size:", font=("Helvetica", 14), fg="black", bg="white")

     size_label.grid(row=1, column=3, padx=10)

     tk.Radiobutton(self.root, text="3x3", variable=self.board_size, value=3, bg="white", fg="black",

                    font=("Helvetica", 12), selectcolor="lightgray").grid(row=1, column=4)

     tk.Radiobutton(self.root, text="5x5", variable=self.board_size, value=5, bg="white", fg="black",

                    font=("Helvetica", 12), selectcolor="lightgray").grid(row=1, column=5)

     tk.Radiobutton(self.root, text="7x7", variable=self.board_size, value=7, bg="white", fg="black",

                    font=("Helvetica", 12), selectcolor="lightgray").grid(row=1, column=6)




     new_game_button = tk.Button(self.root, text="New Game", command=self.new_game, bg="gray", fg="black",

                                 font=("Helvetica", 12, "bold"), padx=10, pady=5, relief="raised")

     new_game_button.grid(row=1, column=7, padx=20)




     player_blue_label = tk.Label(self.root, text="Blue Player", font=("Helvetica", 14, "bold"), fg="blue",

                                  bg="white")

     player_blue_label.grid(row=2, column=0)

     tk.Radiobutton(self.root, text="S", variable=self.current_letter, value="S", bg="white", fg="blue",

                    font=("Helvetica", 12), selectcolor="lightgray").grid(row=3, column=0)

     tk.Radiobutton(self.root, text="O", variable=self.current_letter, value="O", bg="white", fg="blue",

                    font=("Helvetica", 12), selectcolor="lightgray").grid(row=4, column=0)


     player_blue_character = tk.Label(self.root, text="Player Mode", font=("Helvetica", 14, "bold"), fg="blue",

                                  bg="white")

     player_blue_character.grid(row=6,column=0)

     tk.Radiobutton(self.root, text="Human", variable=self.current_blue_player, value="H", bg="white", fg="blue",

                    font=("Helvetica", 12), selectcolor="lightgray").grid(row=7, column=0)

     tk.Radiobutton(self.root, text="Computer", variable=self.current_blue_player, value="C", bg="white", fg="blue",

                    font=("Helvetica", 12), selectcolor="lightgray").grid(row=8, column=0)



     player_red_label = tk.Label(self.root, text="Red Player", font=("Helvetica", 14, "bold"), fg="red",

                                 bg="white")

     player_red_label.grid(row=2, column=6)

     tk.Radiobutton(self.root, text="S", variable=self.red_letter_var, value="S", bg="white", fg="red",

                    font=("Helvetica", 12), selectcolor="lightgray").grid(row=3, column=6)

     tk.Radiobutton(self.root, text="O", variable=self.red_letter_var, value="O", bg="white", fg="red",

                    font=("Helvetica", 12), selectcolor="lightgray").grid(row=4, column=6)


     player_red_character = tk.Label(self.root, text="Player Mode", font=("Helvetica", 14, "bold"), fg="red",

                                  bg="white")

     player_red_character.grid(row=6,column=6)

     tk.Radiobutton(self.root, text="Human", variable=self.current_red_player, value="H", bg="white", fg="red",

                    font=("Helvetica", 12), selectcolor="lightgray").grid(row=7, column=6)

     tk.Radiobutton(self.root, text="Computer", variable=self.current_red_player, value="C", bg="white", fg="red",

                    font=("Helvetica", 12), selectcolor="lightgray").grid(row=8, column=6)
     

     self.difficulty = tk.Scale(self.root, from_=0, to=100, variable=self.game_logic.difficult, orient="horizontal")
     self.difficulty.grid(row=6+5, column = 1+int(5/2))

     self.create_board()




# Everything below here is the code that I changed to meet the crieria for the assignment

# this sets a new board each time and allows the players to interact

# Source: https://stackoverflow.com/questions/6981717/pythonic-way-to-combine-for-loop-and-if-statement


 def create_board(self):

     for widget in self.root.winfo_children():

         if isinstance(widget, tk.Button) and widget.cget("text") != "New Game":

             widget.destroy()




     size = self.board_size.get()

     self.game_logic.reset(size)

     self.board = [[None for _ in range(size)] for _ in range(size)]




     for row in range(size):

         for col in range(size):

             # this will create a button for each cell on the board

             button = tk.Button(self.root, text=" ",

                                width=6, 

                                height=2, 

                                font=("Arial", 16, "bold"),

                                 

                                fg="black",

                                relief="ridge",

                                command=lambda r=row, c=col: self.make_move(r, c))

             button.grid(row=row + 5, column=col + 1, padx=5, pady=5)



     self.turn_label = tk.Label(self.root, 

                                text=f"Current turn: {self.current_player}", 

                                font=("Arial", 14),

                                 

                                )

     self.turn_label.grid(row=2, column=2, columnspan=4)

     if self.current_player == 'Blue' and self.current_blue_player.get() == "C":

         self.comp_play()

     elif self.current_player == 'Red' and self.current_red_player.get() == "C":

         self.comp_play()


 # this resets the game to its initial state

 def new_game(self):

     self.current_player = "Blue"

     self.create_board()




 # this class is responsoble for executing and validating player actions, tracking scores and turns, and applying the specific rules of each game mode

 def make_move(self, row, col):

     
     # this places the board based on the current player and gets the current player to place

     letter = self.current_letter.get() if self.current_player == "Blue" else self.red_letter_var.get()

     

     if self.game_logic.make_move(row, col, letter):

         button = self.root.grid_slaves(row=row + 5, column=col + 1)[0]

         # sets color of button based on the player selected

         if self.current_player == "Blue":

           color = "blue" 

         

         else:

           color = "red"

        
         # updates the button, sets text colot and disables the button

         button.config(text=letter, state="disabled", disabledforeground=color)



       # this will verify an see if an SOS has been formed

         if self.check_for_sos(row, col, letter):

             if self.current_player == 'Blue':

                 self.game_logic.blue_score += 1

             else:

                 self.game_logic.red_score += 1
             
             print(self.game_logic.blue_score, ":" ,self.game_logic.red_score)

             # For Simple Mode: once an SOS has been formed the game will end and declare a winner

             if self.mode.get() == 'Simple':

                 for i in range (self.game_logic.board_size):
                     print(self.game_logic.board[i])
                 self.declare_winner()

            

             # For General game: once all cells are filled a winner will be declared who ever has the most SOS formations

         else:

             self.current_player = 'Red' if self.current_player == 'Blue' else 'Blue'

             self.turn_label.config(text=f'Current turn: {self.current_player}')

         if self.game_logic.all_cells_filled():

             self.declare_winner()
                 
        
         self.game_logic.board[row][col] = letter
         if self.current_player == 'Blue' and self.current_blue_player.get() == "C":
       
            self.comp_play()
       
         elif self.current_player == 'Red' and self.current_red_player.get() == "C":
       
            self.comp_play()

        # will switch player if no winning move has been made


 def generate_actions(self):

       actions = []

       size = self.game_logic.board_size

       for row in range(size):

             for col in range(size):

                 if self.game_logic.board[row][col] == None:

                       for character in ["S", "O"]:

                           actions.append([row, col, character])
       return actions

 

 def computer_check_win(self, actions):

     win_conditions = []

     board = self.game_logic.board

     S_patterns = [

         [(0, -2), (0, -1), (0, 0)],

         [(0, 0), (0, 1), (0, 2)],

         [(-2, 0), (-1, 0), (0, 0)],

         [(0, 0), (1, 0), (2, 0)],

         [(-2, -2), (-1, -1), (0, 0)],

         [(0, 0), (1, 1), (2, 2)],

         [(0, 0), (-1, 1), (-2, 2)],

         [(0, 0), (1, -1), (2, -2)]

        

     ]

     O_patterns = [

         [(1, 0), (0, 0),  (-1, 0)],

         [(0, 1), (0, 0),  (0, -1)],

         [(1, 1), (0, 0),  (-1, -1)],

         [(1, -1), (0, 0),  (-1, 1)],

        

     ]

     for i in range(len(actions)):

       row, col, _ = actions[i]

       if _ == "S":

           for pattern in S_patterns:

               try:



                   letters = []
                   for dr, dc in pattern:
                       if row + dr >= 0 and col + dc >= 0:
                           if dr == 0 and dc == 0:
                               letters.append(_)
                               continue
                           else:
                               letters.append(board[row + dr][col + dc])     
     


                   # if an SOS if formed in any order it will return True

                   if letters == ['S', 'O', 'S']:
                       win_conditions.append([row, col, _])

               except IndexError:



                   # if the pattern is invalid, it skips

                   continue



                   # no SOS found will return False


       else:

           for pattern in O_patterns:

               try:



                   letters = []
                   for dr, dc in pattern:
                       if row + dr >= 0 and col + dc >= 0:
                           if dr == 0 and dc == 0:
                               letters.append(_)
                           else:
                               letters.append(board[row + dr][col + dc])        
     


                   # if an SOS if formed in any order it will return True

                   if letters == ['S', 'O', 'S']:

                       win_conditions.append([row, col, _])

                       

               except IndexError:



                   # if the pattern is invalid, it skips

                   continue



                   # no SOS found will return False"""

     return win_conditions


 def random_decision(self, actions):

     decision = False

     tries = 0

     while decision == False and tries <= int((self.difficulty.get()/100) * 15):

         decision = True

         tries += 1

         row, col, state = random.choice(actions)
         if state == "S":
             t = "O"
         else:
             t = "S"
         check_surrounds = [[row+1,col+1, t],[row+1,col, t],[row,col+1, t],[row-1,col-1, t],[row-1,col, t],[row,col-1, t],[row+1,col-1, t],[row-1,col+1, t], [row+2,col+2, t],[row+2,col, t],[row,col+2, t],[row-2,col-1, t],[row-2,col, t],[row,col-2, t],[row+2,col-2, t],[row-2,col+2, t]]


         if self.game_logic.board[row][col] == None:
             self.game_logic.board[row][col] = state
    
    
             check_surrounds = self.computer_check_win(check_surrounds)
    
             
    
             self.game_logic.board[row][col] = None

         print(tries)
         if len(check_surrounds) != 0:

             decision = False

     return row,col,state


 def comp_play(self):

     actions = self.generate_actions()

     if len(actions) != 0:


           if ((self.difficulty.get()/100) * .9)+.1 >= random.random():

               win_array = self.computer_check_win(actions)

               print(win_array)
               if len(win_array) == 0:


                   print("failed")

                   row, col, state = self.random_decision(actions)


               else:

                   print("score")

                   row, col, state = random.choice(win_array)


           else:

               print("rand")

               row, col, state = self.random_decision(actions)


           if self.current_player == 'Blue' and self.current_blue_player.get() == "C":

               self.current_letter.set(state)

               self.make_move(row, col)

           elif self.current_player == 'Red' and self.current_red_player.get() == "C":

               self.red_letter_var.set(state)
               
               self.make_move(row, col)



 def declare_winner(self):

     if self.mode.get() == 'Simple':

          # Simple mode: first SOS formed will win
          if self.game_logic.blue_score > self.game_logic.red_score:

              

              
              winner_message = f"{self.current_player} wins by forming the first SOS!"

          elif self.game_logic.red_score > self.game_logic.blue_score:

              
              winner_message = f"{self.current_player} wins by forming the first SOS!"

          else:

              winner_message = "Its a draw!"

     else:

         

         # General game: whoever has the most SOS formations will be declared winner

         if self.game_logic.blue_score > self.game_logic.red_score:

             

             winner_message = "Blue Wins!"

         elif self.game_logic.red_score > self.game_logic.blue_score:

             winner_message = "Red Wins!"

         else:

             winner_message = "Its a draw!"


     messagebox.showinfo('Game Over', winner_message)

     # board will reset after a winner has been declared

     self.create_board()

    

 def setUp(self):

     self.rppt = tk.Tk()

     self.game_logic = SOSGame(self.root)










 def check_for_sos(self, row, col, letter):

     size = self.board_size.get()

     board = self.game_logic.board

   # all of the possible SOS patterns that are valid to win

     S_patterns = [

         [(0, -2), (0, -1), (0, 0)],

         [(0, 0), (0, 1), (0, 2)],

         [(-2, 0), (-1, 0), (0, 0)],

         [(0, 0), (1, 0), (2, 0)],

         [(-2, -2), (-1, -1), (0, 0)],

         [(0, 0), (1, 1), (2, 2)],

         [(0, 0), (-1, 1), (-2, 2)],

         [(0, 0), (1, -1), (2, -2)]

        

     ]

     O_patterns = [

         [(1, 0), (0, 0),  (-1, 0)],

         [(0, 1), (0, 0),  (0, -1)],

         [(1, 1), (0, 0),  (-1, -1)],

         [(1, -1), (0, 0),  (-1, 1)],

        

     ]



   # this checks the current SOS pattern and see if it matches the current position the row and column

   # Source: https://www.geeksforgeeks.org/python-try-except/

     if board[row][col] == "S":

       for pattern in S_patterns:

           try:

               letters = []
               for dr, dc in pattern:
                   if row + dr >= 0 and col + dc >= 0:
                       
                       letters.append(board[row + dr][col + dc])        
 


               # if an SOS if formed in any order it will return True

               if letters == ['S', 'O', 'S']:
                   print(row, col, pattern, letters)
                   return True

           except IndexError:



               # if the pattern is invalid, it skips

               continue



               # no SOS found will return False


     else:

       for pattern in O_patterns:

           try:


               letters = []
               for dr, dc in pattern:
                   if row + dr >= 0 and col + dc >= 0:
                       
                       letters.append(board[row + dr][col + dc])        
 


               # if an SOS if formed in any order it will return True

               if letters == ['S', 'O', 'S']:
                   print(row, col, pattern, letters)
                   return True

           except IndexError:



               # if the pattern is invalid, it skips

               continue



               # no SOS found will return False"""


     return False











# Create the game window

root = tk.Tk()
game = SOSGame(root)
root.mainloop()


