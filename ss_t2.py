n = 'y'
while n.lower() in ['y', 'yes']:
    try:
        a1 = float(input('1 side of the 1 envelope: '))
        a2 = float(input('2 side of the 1 envelope: '))
        b1 = float(input('1 side of the 2 envelope: '))
        b2 = float(input('2 side of the 2 envelope: '))
        eq1 = (a1 >= b1 and a2 >= b2) or (a1 >= b2 and a2 >= b1)
        eq2 = (b1 >= a1 and b2 >= a2) or (b1 >= a2 and b2 >= a1)
        if eq1 or eq2:
            print('Yes you can put the envelope in the other one')
        else:
            print('No no, cannot do that')
        n = input('Wanna continue? ')
    except ValueError:
        print('Write integer parameters')
