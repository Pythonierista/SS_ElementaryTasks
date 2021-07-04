import argparse


class Fibonacci:

    def __init__(self, start, end):
        self.s = start
        self.e = end

    def f(self):
        lst = [0, 1, 1]
        while self.s > lst[0]:
            lst = lst[1:].append(lst[-1] + lst[-2])
        while self.e > lst[-1]:
            lst = lst.append(lst[-1] + lst[-2])
        return lst


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('start')
    parser.add_argument('end')
    args = parser.parse_args()

    try:
        args.start, args.end = float(args.start), float(args.end)
        if args.start <= args.end:
            print(*Fibonacci(args.start, args.end).f())
        else:
            print('First number must be less or equal to the second')
    except ValueError:
        print('Please enter digits to calculate Fibonacci sequence')


if __name__ == '__main__':
    main()
