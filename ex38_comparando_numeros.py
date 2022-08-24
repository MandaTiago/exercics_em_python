num = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num < num2:
    print('O número {} é maior que {}!'.format(num2, num))
elif num > num2:
    print('O número {} é maior que {}!'.format(num, num2))
else:
    print('Os dois números são iguais!')