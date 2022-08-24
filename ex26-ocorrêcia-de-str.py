from distutils.filelist import findall


frase = str(input('Digite uma frase: ')).lower().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('a')+1))
print('A ultima ocorrência de A foi na posição {}.'.format(frase.rfind('a')+1))