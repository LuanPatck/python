tem = float(input('Digite uma temperatura:'))
print('A temperatura digitada foi {}\n'
      '{}°C (Celsius)\n'
      '{}°F (Fahrenheit)\n'
      '{}k (Kelvin)'.format(tem, tem, (tem * 1.8)+32, tem + 273.15))