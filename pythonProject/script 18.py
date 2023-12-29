import math
a = float(input('Qual o angulo:'))
se = math.sin(math.radians(a))
co = math.cos(math.radians(a))
ta = math.tan(math.radians(a))
print('Para o ângulo de {}° o seno é {:.2f}\n'
      'Para p ângulo de {}° o coseno é {:.2f}\n'
      'Para o ângulo de {}° a tangente é {:.2f}'.format(a, se, a, co, a, ta))