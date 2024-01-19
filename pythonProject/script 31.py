dis = int(input('Qual a distância de viagem?'))

if dis >= 200:
    print('Você pagarar {:.00f},00 reais'.format((dis * 0.5)))
else:
    print('Você pagarar {:.00f},00 reais'.format((dis * 4.5)))