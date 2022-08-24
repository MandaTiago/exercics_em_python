nota1 = float(input('Qual a sua primeira nota? '))
nota2 = float(input('Qual a sua segunda nota? '))
media = (nota1 + nota2) / 2
if nota1 > nota2:
    print('{} é a maior que!'.format(nota1))
elif nota1 < nota2:
    print('{} é a maior nota!'.format(nota2)) 
else:
    print('Os dois números são iguais!')
if media >= 7:
    print('Sua media foi {}! Você foi APROVADO.'.format(media))
elif media < 7:
    print('A sua media foi {}! Você foi REPROVADO.'.format(media))

