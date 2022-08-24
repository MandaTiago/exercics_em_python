salant = float(input('Qual seu salario? R$'))
salatual = salant + (salant*15/100)
print('Seu salario entigo erá de R${:.2f}, com 15% de aumento seu salário agora é de R${:.2f}'. format(salant, salatual)) 