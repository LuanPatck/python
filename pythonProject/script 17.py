from math import sqrt
co = float(input('Qual o cateto oposto:'))
ca = float(input('Qual o cateto adjacente:'))
hi = sqrt(co**2 + ca**2)
print('A hipotenusa é {:.2f}'.format(hi))

#========outra forma============
#import mach
#hi = mach.hypot(co, ca)