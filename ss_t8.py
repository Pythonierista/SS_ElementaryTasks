import argparse


class Fibonacci:

    def __init__(self, start, end):
        self.s = start
        self.e = end

    def create_fibonacci_array(self):
        lst = [0, 1, 1]
        while self.s > lst[0]:
            lst.append(lst[-1] + lst[-2])
            lst = lst[1:]
        while self.e > lst[-1]:
            lst.append(lst[-1] + lst[-2])
        return lst[:-1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('start', default='1')
    parser.add_argument('end', default='1')
    args = parser.parse_args()

    try:
        args.start, args.end = float(args.start), float(args.end)
        if args.start < args.end:
            print(*Fibonacci(args.start, args.end).create_fibonacci_array())
        else:
            print('First number must be less than the second')
    except ValueError:
        print('Please enter digits to calculate Fibonacci sequence')


if __name__ == '__main__':
    main()
