user = int(input('Qual numero você quer ver na tabuada: '))
for tab in range(1, 10):
    print('{} x {} = {}'.format(user, tab, user*tab))