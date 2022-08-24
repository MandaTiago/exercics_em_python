from time import sleep
peso = float(input('Qual é o seu peso? (kg) '))
altura = float(input('Qual é a sua altura? (m)'))
imc = peso / (altura ** 2)
print('Um momento...')
sleep(1.5)
print('seu imc é de {:.1f}!'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso ideal!')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal! PARABÈNS :) ')
elif imc >= 25 and imc < 30:
    print('Você esta com SOBRESO!')
elif imc >= 30 and imc < 40: 
    print('Você está em OBESIDADE! FIQUE EM ALERTA E PROCURE UM NUTRICIONISTA.')
elif imc > 40:
    print('Você está em OBESIDADE MÒRBIDA, MUITO CUIDADO!')
