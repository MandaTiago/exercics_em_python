from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador processar
print('=' * 30)
print('Vou processar um número de 0 até 5...')
print('=' * 30)
jogador = int(input('Em que numero eu pensei? '))
print('Processando....')
sleep(2)
if jogador == computador:
    print('Parabéns, você consegui acertar!')
else:
    print('Você perdeu! O numero que processei foi {} e o numero que você botou foi {}!'.format(computador, jogador))
