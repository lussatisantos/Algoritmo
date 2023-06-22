a = int(input('Digite o valor de A: '))
b = int (input('Digite o valor de B: '))
c = int(input('Digite o valor de C:'))

print ('A sua equacao e {}x2 + {}x + {} = 0' .format(a, b,c))

delta = b**2 - 4 * a * c

print ('Delta igual {}' .format(delta))

if delta < 0:
    print('Com delta negativo nao tem solucao')
else:
    x = (b-delta**1/2) / 2*a
    x2 = (b+delta**1/2) / 2*a
    print('X1 sera igual a {}'.format(x))
    print('X2 sera igual a {}'.format(x2))