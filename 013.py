#CALCULO DO ALUNO APROVADO E REPROVADO

print ('-'*30)
print ('ESCOLA BOM SAMARITANO')
print ('-'*30)

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
print ('-'*30)

media = (nota1 + nota2) / 2
print ('MEDIA: {}' .format(media))
 
if media > 7:
    print('ALUNO APROVADO')
else:
    print('ALUNO REPROVADO')
print('-'*30)