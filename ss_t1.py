"""Вывести шахматную доску с заданными размерами высоты и ширины, по принципу:
*  *  *  *  *  *
  *  *  *  *  *  *
*  *  *  *  *  *
  *  *  *  *  *  *
Программа запускается через вызов главного класса с параметрами.
"""

import argparse


class Chess:

    INSTRUCTION = 'Please enter positive integers to calculate height and width of the desk'

    def __init__(self, height, width):
        self.h = height
        self.w = width

    def create_chess_deck(self):
        return '\n'.join([' *' * self.w if i % 2 else '* ' * self.w for i in range(self.h)])


def main():
    parser = argparse.ArgumentParser(exit_on_error=False)
    parser.add_argument('-height', type=int)
    parser.add_argument('-width', type=int)

    try:
        args = parser.parse_args()
        if args.height > 0 < args.width:
            print(Chess(args.height, args.width).create_chess_deck())
        else:
            print(Chess.INSTRUCTION)
    except (ValueError, TypeError, argparse.ArgumentError):
        print(Chess.INSTRUCTION)


if __name__ == '__main__':
    main()
