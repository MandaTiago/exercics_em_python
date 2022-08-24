from time import sleep
preco = float(input('Qual foi o valor total da compra? R$'))
print('''Escolha um opção de pagamento:
[1] Valor á vista dinheiro/boleto;
[2] Valor á vista no cartão;
[3] Valor dividido em 2x no cartão;
[4] Valor dividido em 3x ou mais no cartão;''')
opcao = int(input('Qual vai ser oção de pagamento? '))
print('Calculando...')
sleep(1.1)
if opcao == 1:
    total = preco - (preco * 15 / 100)
    print('Sua compra ficará de R${:.2f} com o desconto de 15%!'.format(total))
elif opcao == 2:
    total = preco - (preco * 10 / 100)
    print('Sua compra ficará de R${:.2f} com o descoonto de 10%!'.format(total))
elif opcao == 3:
    total = preco / 2
    print('Sua compra ficará de R${:.2f} dividido em 2x no cartão!'.format(total))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparcela = int(input('Quantas parcelas? '))
    parcela = total / totparcela
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS 20%!'.format(totparcela, parcela))
else:
    total = preco
    print('Opção invalida de pagamento! tente novamente.')
print('O valor de R${:.2f} vai custar R${:.2f} no final!'.format(preco, total))
