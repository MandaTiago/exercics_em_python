numero = int(input('Digite qualquer numero: '))
resultado = numero % 2
if resultado == 0: 
    print('O número {} é PAR!'.format(numero))
else:
    print('O número {} é IMPAR!'.format(numero))