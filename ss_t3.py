
class Triangle:

    def __init__(self, name, side_a, side_b, side_c):
        self.n = name
        self.a = float(side_a)
        self.b = float(side_b)
        self.c = float(side_c)

    def square(self):
        p = (self.a + self.b + self.c) * .5
        return round((p * (p - self.a) * (p - self.b) * (p - self.c)) ** .5, 2)


def main():
    triangles = []
    n = 'y'
    while n.lower() in ['y', 'yes']:
        try:
            triangles.append(Triangle(*[i.strip() for i in input('Enter a triangle ').split(',')]))
        except (TypeError, ValueError):
            print('Please enter the name and 3 sides of a triangle separating by ","')
        n = input('Wanna continue? ')
    print('============= Triangles list: ===============')
    for i, t in enumerate(sorted(triangles, key=lambda x: x.square(), reverse=True)):
        print(f'{i + 1}. [Triangle {t.n}]: {t.square()} сm')


if __name__ == '__main__':
    main()
