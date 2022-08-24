from time import sleep
from datetime import date
atual = date.today().year
nascimento = int(input('Em que ano você nasceu? '))
idade = atual - nascimento
print('Processando...')
sleep(1.5)
print('=-'*20)
if idade <= 9:
    print(' Atleta de {} anos Classifição INFANTIL!'.format(idade))
elif idade > 9 and idade <= 14:
    print('Atleta de {} anos Classificação MIRIN!'.format(idade))
elif idade > 14 and idade <=19:
    print('Atleta de {} anos Classificação JUNIOR!'.format(idade))
elif idade > 19 and idade <=25:
    print('Atleta de {} anos Classificação SÊNIOR!'.format(idade))
elif idade > 25:
    print('Atleta de {} anos Classificação MASTER!'.format(idade))
print('=-'*20)
