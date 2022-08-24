print('{:=^40}'.format('Lojas Pantanal'))
preco = float(input('Qual o preço das compras? R$'))
print('''FORMAS DE PAGAMENTO:
[1] À vista dinheiro, cheque ou pix
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual sua opção de pagamento? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS!'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparcela = int(input('Quer dividir em quantas parcelas? '))
    parcela = total / totparcela
    print('Sua compra será parcelada em {}x de {:.2f} COM JUROS!'.format(totparcela, parcela))
else:
    total = preco
    print('Opção invalida de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preco, total))
