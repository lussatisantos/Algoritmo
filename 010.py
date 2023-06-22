#Para calcular o IMC = massa / altura ao quadrado
# Peso ideal o IMC varia de 18.5 e 25

peso = float(input('Informe a massa (kg): '))
altura = float (input('Informe a sua altura: '))

imc = peso / altura**2

print ('O seu IMC e de {} ' .format(imc))

if imc > 18.5 and imc < 25:
    print('Parabens, voce esta no seu peso ideal')
else:
    print('Voce nao esta no seu peso ideal')