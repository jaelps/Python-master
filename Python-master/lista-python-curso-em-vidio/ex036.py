casa = float(input('Digite o valor da residencia:\n'))
anos = int(input('Sera pago em quantos anos:\n'))
salario = float(input('Quanto você ganha ao mês:\n'))
tempo = casa / (anos * 12)
minimo = salario *30 / 100

if salario <= minimo:
    print('Emprestimo foi negado pois ultrapassa 30% do  seu salario')
else:
    print(f'Imprestimo aprovado, você vai pagar {anos}anos  de R$:{tempo}')

