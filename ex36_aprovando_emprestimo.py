from tkinter import E


casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o salario do comprador? R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12) #Se eu multiplicar o valor de 'anos' por 12 eu vou ter a quantidade de meses que ele vai pagar. ja eu dividindo o valor de 'casa' por (anos * 12) vou ter o valor da prestação de cada mês.
minimo = (salario * 30) / 100 #a prestação da 'casa' não poderá ultrapassar os 30% do salário do comprador, se não o financiamento será negado!
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}!'.format(prestacao))
if prestacao <= minimo:
    print('FINANCIAMENTO CONCEDIDO!')
else: #MAIOR QUE O MINIMO QUER DIZER QUE ULTRAPASSOU OS 30% DO SALARIO E POR ISSO O FINANCIAMENTO ESTÁ NEGADO!
    print('FINANCIAMENTO NEGADO!')