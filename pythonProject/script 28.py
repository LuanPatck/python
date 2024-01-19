from random import randint
from time import sleep
num = randint(0, 10)
print('=-=-' * 10)
print('Tente adivinhar no número que estou pensando')
print('=-=-' * 10)
chu = int(input('Qual o número que estou pensando:'))
print('Processando...')
sleep(2)
if chu == num:
    print('Acertou, o número era {}'.format(num))
else:
   print('Você errou, o número era {}'.format(num))
print(' - FIM - ')