# -*- coding: utf-8 -*-

x = int(input('Please enter the number '))

if x % 4 == 0:
    print('The given number is divided by 4 ')
elif x % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')

check = int(input('Please enter the nummber '))
num = int(input('Please enter another number '))

if check%num == 0:
    print(type(check/num))
else:
    print('Entered numbers do not divide evenly')
