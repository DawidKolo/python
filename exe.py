# -*- coding: utf-8 -*-
slownik = {'kawa': 'czarna', 'herbata':'zielona',  'cukier kostka':4, 0:'zero', 1: 'jeden'}
slownik['herbata']
slownik[0]
type(slownik)
slownik.keys()
list(slownik.keys())
slownik.values()
x = 'herbata' in slownik
print(slownik.keys())
print(list(slownik.keys()))
print(slownik.values())
print('herbata' in slownik)

if x == True:
    print('Kawa jest w slowniku')