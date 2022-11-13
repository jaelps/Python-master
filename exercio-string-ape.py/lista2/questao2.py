frase = input('Frase: \n')

cript = ''

for letra in frase:
    letra = letra.upper()

    if letra == 'A':
        nova = ' '
    elif letra == 'E':
        nova = 'U'
    elif letra == 'I':
        nova = 'O'
    elif letra == 'O':
        nova = 'I'
    elif letra == 'U':
        nova = 'E'
    elif letra == ' ':
        nova = 'A'
    else:
        nova = letra

    cript = cript + nova

print(f'Frase criptografada: {cript}')