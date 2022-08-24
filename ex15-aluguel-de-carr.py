dias = int(input('Quantos dias você alugou o carro? '))
km = float(input('Quantos km rodados? '))
rst = (dias * 60) + (km * 0.15)
print('total a pagar: R${:.2f}'.format(rst))
