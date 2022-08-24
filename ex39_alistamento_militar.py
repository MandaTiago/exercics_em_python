from time import sleep
from datetime import date
atual = date.today().year
nasc = int(input('Em que ano você nasceu? '))
idade = atual - nasc
print('''Você é do gênero masculino ou feminino?
[1] Masculino!
[2] Feminino!''')
gen = int(input('Sua resposta: '))
if idade == 18 and gen == 1:
    print('Quem nasceu em {} tem {} em {}.'.format(nasc, idade, atual))
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18 and gen == 1:
    print('Quem nasceu em {} tem {} em {}.'.format(nasc, idade, atual))
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento vai ser em {}.'.format(ano))
elif idade > 18 and gen == 1:
    print('Quem nasceu em {} tem {} em {}.'.format(nasc, idade, atual))
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento será em {}.'.format(ano))
elif gen == 2:
    print('Você está isenta do alistamento! Obrigado.')
else:
    print('Não foi possível entender sua resposta. Tente novamente!')

