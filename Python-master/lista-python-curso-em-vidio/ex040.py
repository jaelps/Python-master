primeraN = float(input('Nota 1: '))
segundoN = float(input('Nota 2: '))

media = (primeraN + segundoN) / 2

if media < 5.0:
    print(f'Sua media é {media}, Você esta REPROVADO')
elif 7 > media >= 5 :
    print(f'Sua media é {media}, Você esta em RECUPERAÇÃO')
elif media >= 7.0:
    print(f'Sua media {media}, você esta APROVADO')
else:
    print('erro')
