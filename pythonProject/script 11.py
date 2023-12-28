print('====== Bem vindo a calculadora de tinta =======')
a = float(input('Qual a altura da sua parede:'))
b = float(input('Qual o comprimento da dua parede:'))
print('\nConciderando a altura {} e o comprimento {}, sua parede tem {}m²\n'
      'Serão precisos {}l de tinta considerando o rendimento de 2m²/l\n'
      'Sendo preciso {} latas de tintas de 2l'
      .format(a, b, a*b,(a*b)/30, (((a*b)//30)+(a*b)%30)))