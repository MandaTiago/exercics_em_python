salario = float(input('Digite seu salario atual R$'))
if salario <= 1200:
    aumento = salario + (salario * 15 / 100)
else:
    aumento = salario + (salario * 10 / 100)
print('O seu salario que era de R${:.2f}, amentou para R${:.2f}!'.format(salario, aumento))