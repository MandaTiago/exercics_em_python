from time import sleep
velocidade = float(input('Qual a velocidade atual do carro? '))
print('PROCESSANDO...')
sleep(2)
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print('Tenha um bom dia e dirija com responsabilidade!')
else:
    print('Você levou uma multa de R${:.2f} por ultrapassar o limite de velocidade que 80km/h! \n Considerando que a multa é realizada ao decorrer de cada km passado é muliplicado por R$7,00. \n'.format(multa))

    