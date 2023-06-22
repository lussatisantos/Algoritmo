#Para calcular o IMC = massa / altura ao quadrado

#abaixo de 17: muito abaixo do peso
#entre 17 e 18.4: abaixo do peso
#entre 18.5 e 25: peso ideal
#entre 26 e 30: sobrepeso
#entre 31 e 35: obesidade
#entre 36 e 40: obesidade severa
#entre 41 ou mais: obesidade morbida

peso = float(input('Informe o seu peso (kg): '))
alt = float(input('Informe a sua altura: '))
imc = peso / alt**2

if imc < 17:
    print ('Voce esta muito abaixo do peso')
else:
    if imc > 16 and imc < 18.5:
        print ('Voce esta abaixo do peso')
    else:
        if imc > 18.4 and imc < 26:
            print ('Parabens, voce esta no seu peso ideal')
        else:
            if imc > 25 and imc < 31:
                print('Voce esta com sobrepeso')
            else:
                if imc > 30 and imc < 36:
                    print ('Voce esta com obesidade')
                else:
                    if imc > 34 and imc < 41:
                        print('Voce esta com obesidade severa')
                    else:
                        if imc > 40:
                            print('Voce esta com obesidade morbida')