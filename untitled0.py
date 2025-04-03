# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 17:56:59 2025

@author: hrutv
"""

#practcing problems

#print first 10 nos
#for i in range(1,11):
 #   print(i)
 
#a = int(input("enter a number :"))
#if a % 2 == 0:
#    print("entered number is even")
#else:
#    print("entered number is odd")

#string = input("enter s atring :")

#for i in len(string)/2:
#reverse = string[::-1]
#print(reverse)  

#def Reverse_func(s):
#    s = list(s)
#    n = len(s)
#    
#    for i in range(n//2):
#        s[i],s[n-i-1] = s[n-i-1],s[i]
#        
#    return "".join(s)

#print(Reverse_func("Hello"))


#list1 = [1,3,5,7,6,8,19]

#print(max(list1))

import math

def Prime(num):
    if num < 2:
        print("number is not a prime")
        
    for i in range(2, int(math.sqrt(num))+1):
           if num % i == 0:
               print("it is not a prime number")
           
           print("it is a prime no")
        
Prime(10)



  