#!/usr/bin/env python
# coding: utf-8

# In[1]:


n = int(input("enter the number of terms you want in the fibonacci sequence: "))
a = 0
b = 1
if(n <= 0):
    print("please enter a number greater than 0")
elif(n == 1):
    print(a)
elif(n == 2):
    print(a ,b)
else:
    l1 = [a, b]
    while(n-2!=0):
        n-=1
        c = a + b
        a = b
        b = c
        l1.append(c)
    print(l1)

