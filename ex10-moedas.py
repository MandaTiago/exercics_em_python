real = float(input('Quanto você tem na carteira? '))
dolar = real / 5.30
euro = real / 5.96
print('Com o valor de R${:.2f} você poderá comprar US${:.2f} ou £{:.2f}!'.format(real, dolar, euro))