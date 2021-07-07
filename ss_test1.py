import unittest
from ss_t1 import *


class TestChess (unittest.TestCase):

    def test_create_desk(self):
        desk = Chess(3, 5)
        self.assertEqual(desk.h, 3)
        self.assertEqual(desk.w, 5)

    def test_check_desk(self):
        self.assertEqual(Chess(3, 3).create_chess_deck(), '* * * \n * * *\n* * * ')
        self.assertEqual(Chess(1, 5).create_chess_deck(), '* * * * * ')
        self.assertEqual(Chess(4, 2).create_chess_deck(), '* * \n * *\n* * \n * *')

    def test_errors(self):
        with self.assertRaises(TypeError):
            Chess(3, 5.5).create_chess_deck()
            Chess('fds', 6).create_chess_deck()


if __name__ == '__main__':
    unittest.main()
