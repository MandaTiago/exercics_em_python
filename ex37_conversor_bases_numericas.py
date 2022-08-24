from time import sleep
numero = int(input('Digite um número ineiro: '))
print('''Escolha em que base você quer converter:
Digite [1] para binário!
Digite [2] para octal!
Digite [3] para hexadecimal!''')
escolha = int(input('Sua escolha: '))
print('Processando...')
sleep(1)
if escolha == 1:
    print('O {} convertido para base binária é {}!'.format(numero, bin(numero)[2:]))
elif escolha ==2:
    print('O {} convertido para Octal é {}!'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('O {} convertido para Hexadecimal é {}!'.format(numero, hex(numero)[2:]))
else:
    print('Algo deu errado, tente novamente!')