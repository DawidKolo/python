# -*- coding: utf-8 -*-

def function():
    age = int(input('Ile masz lat? '))
    if 18 <= age < 110:
            print('Jesteś pełnoletni')
    elif age < 18:
        x = (18 - age) 
        print('Będziesz pełnoletni za '+str(x)+' lat')
    else:
        print('Ludzie tyle nie żyją!')

try:
    function()    

except: print('Następnym razem podaj liczbę')
function()