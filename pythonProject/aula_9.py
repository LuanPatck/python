#aula de manipulação de strig

frase = 'Engenharia de Aquicultura'

print(frase[3:])  # pega a partir do 3 elemento
print(frase[2:4])  # pega a partir do 3 elemento até o 4, sempre um a menos
print(frase[2:10:3])  # pega a partir do 2 elem. até 10, pulando de 3 em 3
print(frase[1::3])  # pega a partir dp 1 elem. até o último, pulando de 3 em 3
print(frase[:6])  # pega desde do inicio até o 6

# função len, conta os caracteres
print(len(frase))

# função count, identifica quantos vez caracteres especificos
print(frase.count('A'))
print(frase.count('a', 0, 10))  # conta quantos '1' tem de 0 a 10

# função find, localiza e mostras onde começa
print(frase.find('qu'))

# operador 'in' diz que existe ou não, -1
print('de' in frase)

#função de replace, substituie algo
print(frase.replace('de', 'o'))

print(frase)

#função upper, transforma em maiscúlo
print(frase.upper())

#função lower, transforma minuscúlo
print(frase.lower())

# função  capitalize(), Deixa somente a primeira letra em maiúsculo
print(frase.capitalize())

# função  title(), Deixa o primeiro caractere de cada palavra em maiúsculo
print(frase.title())

# função strip(), remove os espacos do ínicio e final da frase, mais não entre as palavras
frase1 = '  engenharia de aquicultura  '
print(frase1.strip())

# rstrip(), remove os espaços somente a direita
print(frase1.rstrip())
# lstrip(), remove os espaços somente a esquerda
print(frase1.lstrip())