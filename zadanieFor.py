# -*- coding: utf-8 -*-

sum = 0

for n in range(1,11):
    sum = sum + n
    print(sum)

cube = 0

for n in range(1,11):
    cube = pow(n,3)
    print(cube)


x = str(input('podaj imiona gości '))
for i in x.split():
    print('Czesc', i)


petla = int(input('Podaj liczbę naturalną '))

for i in range(1, petla):
    if i % 3 == 0 and i % 4 == 0:
        print('hurra', i)
    else:
        print('*')

def holidaybush(n):
    z = n - 1
    x = 1
    for i in range(n):
        print(' ' * z + '+' * x + ' ' * z)
        x+=2
        z-=1
holidaybush(5)