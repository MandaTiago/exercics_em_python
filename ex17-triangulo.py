'''opção = float(input('Digete a medida do cateto oposto: '))
adj = float(input('Digite a medida do cateto adjacente: '))
hipotenusa = op + adj
print('A hipotenusa é: {:.2f}mm!'.format(hipotenusa))'''

import math 
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Compimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa desse triângulo é {:.2f}'.format(hi))