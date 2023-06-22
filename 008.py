ano_actual = int(input('Digite o ano actual: '))
ano_nasc = int(input('Digite o ano de nascimento: '))
idade = ano_actual - ano_nasc

print ('Em {} voce tera {} anos de idade' .format(ano_actual, idade))

if idade < 12:
    print('Voce seras uma crianca')
else:
    if idade > 12 and idade < 17:
        print ('Voce seras um adolescente')
    else:
        if idade > 17 and idade < 35:
            print ('Voce seras jovem')
        else:
            if idade > 35 and idade < 60:
                print('Voce seras adulto')
            else:
                if idade > 60:
                    print ('Voce seras idoso')