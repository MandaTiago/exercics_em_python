'''import math
angulo = float(input('Digite um angulo que você deseja: '))
sen = math.sin(math.radians(angulo))
print('O ângulo de {} tem o seno de {:.2f}!'.format(angulo, sen))
cos = math.cos(math.radians(angulo))
print('O ângulo de {} tem o coseno de {:.2f}!'.format(angulo, cos))
tan = math.tan(math.radians(angulo))
print('O angulo de {} tem a tangente de {:.2f}!'.format(angulo, tan))'''


from math import radians, sin, cos, tan
angulo = float(input('Digite um angulo que deseja: '))
sen = sin(radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}!'.format(angulo, sen))
cose = cos(radians(angulo))
print('O angulo de {} tem o COSENO de {:.2f}!'.format(angulo, cose))
tang = tan(radians(angulo))
print('O angulo de {} tem a TANGENTE de {:.2f}!'.format(angulo, tang)) 