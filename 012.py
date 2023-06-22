#CALCULO DE CARTEIRA DE MOTORISTA

print ('-'*28)
print('DEPARTAMENTO DE TRANSITO')
print ('-'*28)

ano_actual = int(input('Ano actual (yyyy): '))
ano_nasc = int(input('Ano de nascimento (yyyy): '))
idade = ano_actual - ano_nasc

print ('-'*9 ,' STATUS ' ,'-'*9)
print ('IDADE: {} ANOS' .format(idade))

if idade < 17:
    print ('N/APTO A TIRAR A CARTEIRA')
else:
    print('APTO A TIRAR A CARTEIRA')
print ('-'*28)