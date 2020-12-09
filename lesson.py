# -*- coding: utf-8 -*-
listaSeriali = {'Lost':'7/10', 'Battlestar Galactica':'8/10', 'The 100':'6/10', 'Space : Above and Beyond': '7/10'}
print(listaSeriali.keys())
pytanie = input('Jaki serial chciałbyś obejrzeć? ')
print(listaSeriali[pytanie])

nowy = input('Jaki seria dodać do Bazy? ')
ocena =  input('Jaką ocenę dajesz? ' + nowy + '? ')
listaSeriali[nowy] = str(ocena)

print(list(listaSeriali.keys()))




