preco = float(input('Qual o preço do produto? R$'))
avista = preco - (preco*15/100)
aprazo = preco + (preco*5/100)
print('O valor R${} no pagamento a vista com desconto de 15% ficará de: R${}, e a prazo ficará de: R${}'.format(preco, avista, aprazo))