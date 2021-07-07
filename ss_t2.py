"""Есть два конверта со сторонами (a,b) и (c,d) определить, можно ли один конверт вложить в другой. Программа должна
обрабатывать ввод чисел с плавающей точкой. Программа спрашивает у пользователя размеры конвертов по одному параметру
за раз. После каждого подсчёта программа спрашивает у пользователя хочет ли он продолжить. Если пользователь ответит
“y” или “yes” (без учёта регистра), программа продолжает работу сначала, в противном случае – завершает выполнение. """


class Envelope:

    def __init__(self, side_a, side_b):
        self.a = side_a
        self.b = side_b

    def __lt__(self, other):
        return self.a < other.a and self.b < other.b or self.a < other.b and self.b < other.a

    def __gt__(self, other):
        return self.a > other.a and self.b > other.b or self.a > other.b and self.b > other.a


def main():
    n = 'y'
    while n.lower() in ['y', 'yes']:
        try:
            a = float(input('1 side of the 1 envelope: '))
            b = float(input('2 side of the 1 envelope: '))
            c = float(input('1 side of the 2 envelope: '))
            d = float(input('2 side of the 2 envelope: '))
            env1 = Envelope(a, b)
            env2 = Envelope(c, d)
            if env1 > env2 or env1 < env2:
                print('Yes you can put the envelope in the other one')
            else:
                print('No no, cannot do that')
            n = input('Wanna continue? ')
        except ValueError:
            print('Write integer parameters')


if __name__ == '__main__':
    main()
