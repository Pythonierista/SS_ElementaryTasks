def moscow(t):
    return len(list(filter(lambda x: sum(map(int, list(str(x)[:3]))) == sum(map(int, list(str(x)[3:]))), t)))


def piter(t):
    return len(list(filter(lambda x: sum(filter(lambda y: y % 2, map(int, list(str(x)))))
                    == sum(filter(lambda z: not z % 2, map(int, list(str(x))))), t)))


def main():
    tickets = [i for i in range(100000, 1000000)]
    try:
        with open(input()) as f:
            alg = f.readline()
    except FileNotFoundError:
        print('Please enter an existing file')
    if alg == 'Moskow':
        print(moscow(tickets))
    elif alg == 'Piter':
        print(piter(tickets))
    else:
        print('Please choose a file with "Moscow/Piter" algorithms')


if __name__ == '__main__':
    main()
