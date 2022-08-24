nome = str(input('Digite seu nome completo: ')).strip()
'''up = str(nome.upper(nome))'''
print('Analisando o sistema...')
print('Seu nome com letras maiúsculas fica: {}'.format(nome.upper()))
print('Seu nome com letras minúsculas fica: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
pnome = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras!'.format(pnome[0], len(pnome[0])))