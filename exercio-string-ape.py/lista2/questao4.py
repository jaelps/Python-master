s = str(input('Digite uma frase:  '))
n = int(input('Digite um valor inteiro:   '))

saida = ''

for caracter in s:
    cm = caracter.upper()

    if cm == 'A' or cm =='I' or cm == 'O' or cm == 'U':
        saida = saida + caracter * n
    else:
        saida = saida + caracter

print(f'Saida: {saida}')