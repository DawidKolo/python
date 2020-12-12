# -*- coding: utf-8 -*-

def function():
    age = int(input('How old are you? '))
    if 18 <= age < 110:
            print('You are an adult')
    elif age < 18:
        x = (18 - age) 
        print('You will become an adult in '+str(x)+' year(s)')
    else:
        print('People don\'t live so long')

try:
    function()    

except: print('Just numbers, please')
function()