print('=========Locadora de Carros=======')
km = float(input('Quantos km você percorreu:'))
di = int(input('Quantos dia você está de posse do carro:'))
va = (km * 0.15) + (di * 60)
print('Como você percorreu {}km e passou {} dias com o carro,\n'
      'O valor de aluguel vai ser {}'.format(km, di, va))
