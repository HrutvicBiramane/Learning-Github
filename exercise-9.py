# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 17:19:05 2025

@author: hrutv
"""

#addition of digits using modulus operator
num = int(input("enter a five-digit number :"))

#extraction of digits from it
d1 = num // 10000
d2 = (num % 10000) // 1000
d3 = (num % 1000) // 100
d4 = (num % 100) //10
d5 = num % 10

Sum = d1+d2+d3+d4+d5
print("sum of digits is :",Sum)