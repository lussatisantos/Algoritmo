#Aproveitamento do aluno
#Entre 10 a 9 A
#Entre 8.9 a 8 B
#Entre 7.9 a 7 C
#Entre 6.9 a 6 D
#Entre 5.9 a 5 E
#Abaixo de 5 F

print ('-'*28)
print('Escola Javali Cansado')
print ('-'*28)

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

if media >=9 and media <= 10:
    print('MEDIA: {}'.format(media))
    print('APROVEITAMENTO: A')
else:
    if media < 9 and media >= 8:
        print('MEDIA: {}'.format(media))
        print('APROVEITAMENTO: B')
    else:
        if media < 8 and media >= 7:
            print('MEDIA: {}' .format(media))
            print('APROVEITAMENTO: C')
        else:
            if media < 7 and media >= 6:
                print('MEDIA: {}' .format(media))
                print('APROVEITAMENTO: D')
            else:
                if media < 6 and media >= 5:
                    print('MEDIA: {}' .format(media))
                    print('APROVEITAMENTO: E')
                else:
                    print('MEDIA: {}' .format(media))
                    print('APROVEITAMENTO: F')