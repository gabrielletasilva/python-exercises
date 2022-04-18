tab = int(input('multiplication table of number:'))
for n in range(11):
    print(f'{tab}x{n}={tab*n}')


tab = int(input('multiplication table of number:'))
for n in range(11):
    print('{}x{}={}'.format(tab, n, tab*n))