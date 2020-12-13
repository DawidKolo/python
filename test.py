# -*- coding: utf-8 -*-

def add(a,b):
    addResult = a + b
    return addResult

def subAdd(i,j):
    subResult = i - j
    return subResult

x = int(input('enter number '))
y = int(input('another one '))
z = int(input('and again '))

print('the sum is ',add(x,y))

print('result of the subtraction is ',subAdd(z,add(x,y)))