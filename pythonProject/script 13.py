pro = float(input('Qual salário do funcionário:'))
print('O salário que era de R$ {:.2f} aplicando o aumento de 15% vai passar a ser R$ {:.2f}\n'
      'Aumento de R$ {}'.format(pro, pro+(pro*15/100), (pro*15/100)))