nome = input('Digite seu nome completo:').strip()
print('Analisando seu nome ....')
print('Em maiúsculo: {}'. format(nome.upper()))
print('Em minusculo: {}'.format(nome.lower()))
print('Seu nome tem {} caracteres'.format(len(nome)-nome.count(' ')))