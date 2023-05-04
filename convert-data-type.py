# -*- coding: utf-8 -*-
"""
Created on Thu May  4 10:24:54 2023

@author: ferisa.prestasi
"""

#Convert integer number to a string and float
#assign variable number 

number = 10
#check data type of number, first
print(type(number))
#<class 'int'>

#convert int to string using str() function
#assign to new var conv1 and check type of data conv1
conv1 = str(number)
print(conv1)
print(type(conv1))
#<class 'str'>

#convert int to float using float() function
conv2 = float(number)
print(conv2)
print(type(conv2))
#10.0
#<class 'float'>

#convert conv1 string to integer using int() function
conv3 = int(conv1)
print(conv3)
print(type(conv3))
#10
#<class 'int'>

#convert boolean to integer, automatically assign binary number using int() function
#1 for True, and 0 for False
data1 = True
data2 = False
print(int(data1))
print(type(data1))
print(int(data2))
print(type(data2))
#1
#<class 'bool'>
#0
#<class 'bool'>
