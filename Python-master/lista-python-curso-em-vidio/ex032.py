#import datetime

ano  = int(input('Digite o a no a ser verificado:  '))

#if ano == 0:
    #ano = date.today().year

if (ano % 4) == 0 and (ano % 100) != 0 or (ano % 400) == 0:
    print('O ano é bissexto')
else:
    print('O ano não é bissexto')

#
