from time import sleep
distancia = float(input('Informe a distância que você irá percorrer: '))
print('Você vai percorrer em média {}km!'.format(distancia))
print('\033[32mCalculando o preço da passagem...\033[m')
sleep(3.8)
if distancia > 200: 
    preco = distancia * 0.45
else:
    preco = distancia * 0.50
print('\033[36mO preço da sua passagem será de \033[31mR${:.2f}!\033[m'.format(preco))