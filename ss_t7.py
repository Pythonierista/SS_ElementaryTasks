import argparse


class Sequence:

    def __init__(self, n):
        self.n = n

    def sequence_of_nums(self):
        lst = list(range(1, self.n + 1))
        for i in lst:
            if i ** 2 >= self.n:
                return lst[:lst.index(i)]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('n')
    args = parser.parse_args()

    try:
        args.n = int(args.n)
        if args.n >= 1:
            print(*Sequence(args.n).sequence_of_nums())
        else:
            print('Please enter a positive integer')
    except ValueError:
        print('Please enter a positive integer')


if __name__ == '__main__':
    main()
