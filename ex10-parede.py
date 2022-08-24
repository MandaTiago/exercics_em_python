largura = float(input('Quanto de largura tem sua parede? '))
altura = float(input('Quanto de altura tem sua parede? '))
area = largura * altura
tinta = area / 2
print('A sua parede tem dimensão de {}x{} e sua area é de {:.4f}m².'.format(largura, altura, area))
print('Para pintar sua parede, você precisará de aproximadamente {:.4f}L de tinta.'.format(tinta))
