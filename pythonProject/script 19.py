import random
n1 = str(input('Digite 1º nome:'))
n2 = str(input('Digite 2º nome:'))
n3 = str(input('Digite 3° nome:'))
n4 = str(input('Digite 4° nome:'))
lis = [n1, n2, n3, n4]
so = random.choice(lis)
print('O sorteado foi {}'.format(so))