identificacao = str(input('Digite o seu e-mail: '))

itens = identificacao.split('@')


print(f'E-mail infomrado {identificacao}')
print(f'Login: {itens[0]}')
print(f'Dominio: {itens[1]}')
