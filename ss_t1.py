import argparse


class Chess:

    def __init__(self, height, width):
        self.h = height
        self.w = width

    def create_chess_deck(self):
        return '\n'.join([' *' * self.w if i % 2 else '* ' * self.w for i in range(self.h)])


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-height', default=0)
    parser.add_argument('-width', default=0)
    args = parser.parse_args()

    try:
        args.height, args.width = int(args.height), int(args.width)
        if args.height > 0 < args.width:
            print(Chess(args.height, args.width).create_chess_deck())
    except ValueError:
        print('Please enter positive integers to calculate height and width of the desk')


if __name__ == '__main__':
    main()
