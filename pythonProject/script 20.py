import random
n1 = input('Digite 1° nome:')
n2 = input('Qual o 2° nome:')
n3 = input('Qual o 3° nome:')
n4 = input('Qual o 4° nome:')
lis = [n1, n2, n3, n4]
random.shuffle(lis)

print('A ordem de apresentação será\n',lis)