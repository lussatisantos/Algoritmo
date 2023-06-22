emp = float(input('Quanto queres de emprestimo? '))
valor_emp = (emp * 0.2) + emp

print ('A taxa de juro equivale a 20% e voce pagaras {}AOA' .format(valor_emp))

parcelas = int(input('Quantas parcelas? '))
valor_total = valor_emp / parcelas

print ('Voce vai pagar {} parcelas de {} kwanzas' .format(parcelas, valor_total))