nome = str(input('Digite o nome do Aluno: '))
n1 = float(input('Qual a primeira nota? '))
n2 = float(input('Qual a segunda nota? '))
rs = (n2 + n1) / 2
print('A média de {} é: {:.1f}'.format(nome, rs))