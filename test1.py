
import unittest 
import tkinter as tk
from Sprint4 import GameLogic
from Sprint4 import SOSGame


# Reference: https://stackoverflow.com/questions/6854658/explain-the-setup-and-teardown-python-methods-used-in-test-cases

class TestGameLogic(unittest.TestCase):
    def setUp(self):

        self.root = tk.Tk()
        self.game_logic = SOSGame(self.root)


    
    def test_simple_mode_win(self):
        self.game_logic.mode.set('Simple')

        self.game_logic.current_letter.set('S')
        self.game_logic.make_move(0, 0)
        self.game_logic.current_letter.set('S')
        self.game_logic.make_move(0, 2)

        self.game_logic.current_letter.set('O')
        self.game_logic.make_move(0, 1)


        self.assertEqual(self.game_logic.current_player, 'Blue')

    


    def test_move_on_filled_cell(self):

        self.game_logic.make_move(0, 0)
        result = self.game_logic.make_move(0, 0)
        self.assertFalse(result)

    
    def test_CPUblue(self):

        self.game_logic.board_size.set(3)
        self.game_logic.current_blue_player.set("C")
        self.game_logic.create_board()

        unvacant = 0
        for i in range(self.game_logic.board_size.get()):
            for j in range(self.game_logic.board_size.get()):
                if self.game_logic.game_logic.board[i][j] != None:
                    unvacant += 1
        self.assertTrue(unvacant == 1)

    def test_CPUred(self):

        self.game_logic.board_size.set(3)
        self.game_logic.current_red_player.set("C")
        self.game_logic.create_board()

        self.game_logic.make_move(0, 0)
        unvacant = 0
        for i in range(self.game_logic.board_size.get()):
            for j in range(self.game_logic.board_size.get()):
                if self.game_logic.game_logic.board[i][j] != None:
                    unvacant += 1
        self.assertTrue(unvacant == 2)

    def CPUblue_red_simple(self):
    
        self.game_logic.board_size.set(3)
        self.current_blue_player.set("C")
        self.current_red_player.set("C")
        self.game_logic.create_board()
        unvacant = 0
        for i in range(self.game_logic.board_size.get()):
            for j in range(self.game_logic.board_size.get()):
                if self.game_logic.game_logic.board[i][j] != None:
                    unvacant += 1
        self.assertTrue(self.game_logic.game_logic.all_cells_filled())

    def CPUblue_red_general(self):
    
        self.game_logic.board_size.set(3)
        self.current_blue_player.set("C")
        self.current_red_player.set("C")
        self.game_logic.create_board()
        unvacant = 0
        for i in range(self.game_logic.board_size.get()):
            for j in range(self.game_logic.board_size.get()):
                if self.game_logic.board[i][j] != None:
                    unvacant += 1
        self.assertTrue(unvacant == 9)

    def CPUblue_red_general(self):
    
        self.game_logic.board_size.set(3)
        self.current_blue_player.set("C")
        self.current_red_player.set("C")
        self.game_logic.create_board()
        unvacant = 0
        for i in range(self.game_logic.board_size.get()):
            for j in range(self.game_logic.board_size.get()):
                if self.game_logic.board[i][j] != None:
                    unvacant += 1
        self.assertTrue(unvacant == 9)

    # Reference: https://stackoverflow.com/questions/6854658/explain-the-setup-and-teardown-python-methods-used-in-test-cases

    def tearDown(self):

        self.root.destroy()

if __name__ == '__main__':
    unittest.main()







