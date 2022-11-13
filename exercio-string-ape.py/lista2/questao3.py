nome = str(input('Digite o nome:  ')).upper()

parte = nome.split()
n = len(parte)
saida = parte[n-1] + ', '

for i in range(n-1):
    saida = saida + parte[i][0] + '. '

print(f'Nome formatado: {saida}')