from datetime import date
sexo = str(input('''Informe seu sexo:
 [ M ] para mulher
 [ H ] para homem\n ''')).upper()


if sexo == 'H':

    ano = int(input('Ano de nascimento: '))
    idade = date.today().year - ano
    al = int(idade - 18)


    if idade < 18:
        print(f'Você tem {idade} anos falta {al} para seu alistamento')
    elif idade == 18:
        print(f'Você tem {idade} anos de idade, esta na hora do alistamento')
    else:
        print(f'Já passou {al} do seu alistameto.')


elif sexo == 'M':
    print('Para o mulhes o alistamento é opcional')
    
else:
    print('Invalido, favor repita')
