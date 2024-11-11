import unittest 
import tkinter as tk
from Sprint3 import GameLogic
from Sprint3 import SOSGame


# Reference: https://stackoverflow.com/questions/6854658/explain-the-setup-and-teardown-python-methods-used-in-test-cases

class TestGameLogic(unittest.TestCase):
    def setUp(self):

        self.root = tk.Tk()
        self.game_logic = SOSGame(self.root)


    # Reference: https://stackoverflow.com/questions/6854658/explain-the-setup-and-teardown-python-methods-used-in-test-cases

    def tearDown(self):

        self.root.destroy()

    def test_simple_mode_win(self):

        self.game_logic.mode.set('Simple')
        self.game_logic.make_move(0, 0)
        self.game_logic.current_letter.set('O')
        self.game_logic.make_move(0, 1)
        self.game_logic.current_letter.set('S')
        self.game_logic.make_move(0, 2)


        self.assertEqual(self.game_logic.current_player, 'Blue')
        self.assertEqual(self.game_logic.check_for_sos,(0, 2, 'S'))

    
    


    def test_move_on_filled_cell(self):

        self.game_logic.make_move(0, 0)
        result = self.game_logic.make_move(0, 0)
        self.assertFalse(result)


    def test_general_mode_tie(self):

        self.game_logic.mode.set('General')
        self.game_logic.board_size.set(3)
        self.game_logic.create_board()


        moves = [
            ('S', 0, 0), ('O', 0, 1), ('S', 0, 2),
            ('S', 1, 0), ('O', 1, 1), ('S', 1, 2),
            ('S', 2, 0), ('O', 2, 1), ('S', 2, 2),

        ]

        for letter, row, col in moves:
            self.game_logic.current_letter.set(letter)
            self.game_logic.make_move(row, col)

        self.assertTrue(self.game_logic.all_cells_filled())
        self.assertEqual(self.game_logic.blue_score, self.game_logic.red_score)

class SOSGame:

    def all_cells_filled(self):
        for row in self.board:
            if any(cell == '' for cell in row):
                return False
            return True

if __name__ == '__main__':
    unittest.main()







