vel = int(input('Qual a sua velocidade:'))
if vel <= 80:
    print('Muito bem, continue sua viagem')
else:
    print('Acima da velocidade, permitida')
    print('Multado em {},00 reais'.format((vel-80)*7))
