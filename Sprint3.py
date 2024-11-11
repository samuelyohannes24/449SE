import tkinter as tk
from tkinter import messagebox











class GameLogic:
  def __init__(self, board_size):
      self.board_size = board_size
      self.board = [[None for _ in range(board_size)] for _ in range(board_size)]
      self.blue_score = 0
      self.red_score = 0




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
class SOSGame:
  def __init__(self, root):
      self.root = root
      self.root.title("SOS Game")
      self.root.configure(bg="white")




      self.current_player = "Blue"
      self.current_letter = tk.StringVar(value="S")
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




      player_red_label = tk.Label(self.root, text="Red Player", font=("Helvetica", 14, "bold"), fg="red",
                                  bg="white")
      player_red_label.grid(row=2, column=6)
      tk.Radiobutton(self.root, text="S", variable=self.red_letter_var, value="S", bg="white", fg="red",
                     font=("Helvetica", 12), selectcolor="lightgray").grid(row=3, column=6)
      tk.Radiobutton(self.root, text="O", variable=self.red_letter_var, value="O", bg="white", fg="red",
                     font=("Helvetica", 12), selectcolor="lightgray").grid(row=4, column=6)




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
                                 fg="black", 
                                 )
      self.turn_label.grid(row=2, column=2, columnspan=4)



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
          color = "blue" if self.current_player == "Blue" else "red"

          # updates the button, sets text colot and disables the button
          button.config(text=letter, state="disabled", disabledforeground=color)



        # this will verify an see if an SOS has been formed
          if self.check_for_sos(row, col, letter):
              if self.mode.get() == 'Blue':
                  self.game_logic.blue_score += 1
              else:
                  self.game_logic.red_score += 1

              # For Simple Mode: once an SOS has been formed the game will end and declare a winner
              if self.mode.get() == 'Simple':
                  self.declare_winner()
                  return
             
              # For General game: once all cells are filled a winner will be declared who ever has the most SOS formations
          if self.game_logic.all_cells_filled():
              if self.mode.get() == 'General':
                  self.declare_winner()
              return
             

         # will switch player if no winning move has been made
          self.current_player = 'Red' if self.current_player == 'Blue' else 'Blue'
          self.turn_label.config(text=f'Current turn: {self.current_player}')








  def declare_winner(self):
      if self.mode.get() == 'Simple':
           # Simple mode: first SOS formed will win
           winner_message = f"{self.current_player} wins by forming the first SOS!"
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
      sos_patterns = [
          [(0, -2), (0, -1), (0, 0)],
          [(0, 0), (0, 1), (0, 2)],
          [(-2, 0), (-1, 0), (0, 0)],
          [(0, 0), (1, 0), (2, 0)],
          [(-2, -2), (-1, -1), (0, 0)],
          [(0, 0), (1, 1), (2, 2)],
          [(0, 0), (-1, 1), (-2, 2)],
          [(0, 0), (1, -1), (2, -2)]
         
      ]



    # this checks the current SOS pattern and see if it matches the current position the row and column
    # Source: https://www.geeksforgeeks.org/python-try-except/
      for pattern in sos_patterns:
          try:




              letters = [board[row + dr][col + dc] for dr, dc in pattern]



            # if an SOS if formed in any order it will return True
              if letters == ['S', 'O', 'S']:
                  return True
          except IndexError:



            # if the pattern is invalid, it skips
              continue



              # no SOS found will return False
      return False
















# Create the game window
root = tk.Tk()
game = SOSGame(root)
root.mainloop()



