frase = input('frase:  ')
n = len(frase)

print('Saida: ')

for i in range(n):
    print(frase[i]*(i+1))

for i in range(n-2,-1,-1):
    print(frase[i]*(i+1))