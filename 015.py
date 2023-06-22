#Analise de jogo

print('Manchester City x Real Madrid')
print('-'*25)

city = int(input('Golos do Manchester City: '))
madrid = int(input('Golos de Real Madrid: '))

total = city - madrid

if total == 0:
    print('Diferenca: {}'.format(total))
    print('Status: Empate')
else:
    if total < 4:
        print('Diferenca: {}'.format(total))
        print ('Status: Normal')
    else:
        print ('Diferenca: {}'.format(total))
        print('Status: GOLEADA')                