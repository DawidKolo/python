# -*- coding: utf-8 -*-

def BMI():
    print('*** BMI calc ***')
    
    weight = float(input('Please enter your weight '))
    height = float(input('Please enter your height in centimeters '))
    mHeight = height/100
    x = weight/(pow(mHeight, 2))

    if x < 19:
        print('You are so skinny ')
    elif 19 <= x < 25:
        print('All good mate :) ')
    elif 25 <= x < 30:
        print('Time to sign up to the gym ')
    else:
        print('Just seat, relax and wait for your heart attack ')


try:
    BMI()
except: print('Try again ')
BMI()





