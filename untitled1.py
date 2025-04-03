# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 19:01:48 2025

@author: hrutv
"""

#list1 = [1,1,2,3,4,5]
#print("addition of ele of list is :",sum(list1))
#print("largest ele is :",max(list1))
#print("smallest ele is :",min(list1))

#reverse a list
#def reverse(list1):
#    n = len(list1)
#
#    for i in range(0,n//2):
#        list1[i],list1[n-i-1] = list1[n-i-1],list1[i]
#    return list1
#
#print(reverse(list1))

#count no of coccurance of ele in a list
#def Count(list1):
#    count = {}
#    for i in list1:
#        if i in count:
#            count[i] += 1
#        else:
#            count[i] = 1
#            
#    return count
#
#print(Count(list1))
 
#remove dublicate ele from the list
#def Duplicate(list1):
#    list2 = []
#    for i in list1:
#        if i not in list2:
#              list2.append(i)
#        
#    return list2
#            
#print(Duplicate(list1))

#def even(list1):
#    list2 = []
#    for i in list1:
#        if i % 2 == 0 not in list2:
#            list2.append(i)
#            
#    return list2#
#
#print(even(list1))
              
tup = (1,1,1,2,3,4,5)
#print(len(tup))

#def swap(tup):
#  list1 = list(tup)
#  list1[0],list1[-1] = list1[-1],list1[0]
       
#  tuple2 = tuple(list1)           
#  return tuple2
#print(swap(tup))

#print(list(tup))

list1 = list(tup)
count = []
for i in list1:
    if i==1 in list1:
        count = count + list1
    
    tupl = tuple(list1)
        
print(tupl)
print(tup.count(1))

print(list1.count(2))

#string is palindrome or not

#   s = list(s)
#    n = len(s)
#    
#    for i in range(n // 2):
#        s[i],s[n-i-1] = s[n-i-1],s[i]
#        
#        return "".join(s)    #
#
#def Pali(s):
#    if s == s[::-1]:
#        print("it is a palindrome")
#    else:
#        print("not a palindrome")
#print(Rev("Hello"))
#Pali("AAA")

string = "Hello World"
#print( string[::-1])
#count = 0
#lst = list(string)
#for i in lst:
#    if i == 'e' or i == 'a' or i == 'i' or i == 'o' or i == 'u':
#        count += 1
#print(count)


#count_a = 0
#count_e = 0
#3count_i = 0
#count_o = 0
#count_u = 0

#lst = list(string)
#for i in lst:
#    if i == 'a':
#        count_a += 1
#    elif i == 'e':
#3        count_e += 1
##        count_i += 1
 #   elif i == 'o':
 #       count_o += 1
 #   elif i == 'u':
 #       count_u += 1
 #   else :
 #       print("no vowels found")
#dic = {'a':count_a,'e':count_e,'i':count_i,'o':count_o,'u':count_u}
#print(dic)
   
#print(string.replace(" ",""))
#print(string.isalpha())
         
#d#ec1 = {1:'a',2:'b',3:'c'}
#dec2 = {4:'d',5:'e',6:'f'}
#print(dec1)
#print(dec2)

#dec1.update(dec2)
#print(dec1)
#print(dec1.keys())
#print(dec2.values())
#print(dec1.get(1))


#for i in range (1,101):
#   if i % 3 == 0 and i % 5 == 0:
#       print("FizzBuzz")
#   elif i % 3 == 0:
#         print("Fizz")
#   elif i % 5 == 0:
#            print("Buzz")
#   else:
#            print(i)
    #for i in range(1,101,3,5):
       # print("FizzBuzz")
  

#fibonacci series
#def fibonacci(num):
#    a,b = 0,1
#    while a <= num:
#        print(a,end="")
#        a,b = b,a+b
##        
#n = int(input("enter a value :"))
#fibonacci(n)

#second largest no

#list1 = [1,2,3,4,5,6]
#print(list1)
#if list1[0] > list1[1]:
#    max1 = list1[0]
#    max2 = list1[1]
#else:
#    max1= list1[1]
#    max2 = list1[0]
#    
##for i in range(2,len(list1)):
#    if list1[i] > max1:
#        max2 = max1
#        max1 = list1[i]
##    else:
#3        max2 = list1[i]
#print(max2)
#print(max1)

#stri = "hello worls this is a string" 
#print(stri.swapcase())       
       