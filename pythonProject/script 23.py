num = int(input('Digite um número:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('A unidade do número é {}'.format(u))
print('A dezena do número é {}'.format(d))
print('A centena do número é {}'.format(c))
print('A milhar do número é {}'.format(m))