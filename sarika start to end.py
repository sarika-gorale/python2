#!/usr/bin/env python
# coding: utf-8

# In[2]:


# History

name = "Guido van rossum"

year= 1990




# In[3]:


# variable

s = (1,2,3,4,5)
print(s)


# In[ ]:


# comments

# this is a comment.

""" 
this is a comment.
"""


# In[6]:


# input-output function

s = input("Enter your name")
print(f"my name is {s}")


# In[9]:


# keywords

import keyword
print(keyword.kwlist)


# In[7]:


# operaters

# arithmetic operator

print(5+6)

print(5-6)

print(5*6)

print(5/6)

print(5//6)

print(5%6)


# In[10]:


# logical operator

print( 1 and 0 )

print( 1 or 0 )

print(not 0 )


# In[12]:


# identity operator
   
s = 5
m = 6

print(s is m)

print(s is not m )


# In[13]:


#  membership operator

ss = (1,2,3,4,5,6)

print( 4 in ss)

print(7 not in ss)


# In[14]:


# if_else statement

s = int (input("Enter your age"))

if s>18:
    print("you are eligible for voting")
    
else:
    print("you are not eligible for voting")


# In[17]:


# if_elif_else statement

a = int(input("enter number"))
b = int(input("enter number"))

if a>b:
    print("a is greater than b")
    
elif b<a:
    print("b is less than a")
    
else:
    print("a is not equal to b")


# In[23]:


# nested_if_else statement

bags = input("Enter bag type(skybag, fastrack, ppuma, gucci )")
colors = input("Enter color (red, blue, sky blue, yellow, )")
if bags == "skybag":
    print("skybag price starts from 1500 RS.")
elif bags == "fastrack":
     print("fastrack price starts from 500 RS.")
elif bags == "ppuma":
     print("ppuma price starts from 1000 RS.")
elif bags == "gucci":
     print("gucci price starts from 1900 RS.")
     if colors == "red":
        print(" skybag  bag colors is red, blue, sky blue, yellow, ,")
     elif colors == "blue":
        print(" fastrack bag colors is red, blue, sky blue, yellow, ")
     elif colors == "sky blue":
        print(" ppuma bag colors is red, blue, sky blue, yellow, ")
     elif colors == "yellow":
        print("the bag colors is red, blue, sky blue, yellow, ")
     else:
        print(" this bag is not available")
else:
     print("this bag is not available.")


# In[31]:


# loops

# for loop

for i in range(2,10):
    print(i)
    


# In[51]:


# while loop

i = 2

while i <=10:
    print(i * "1")
    i = i+2


# In[49]:


# function

def sa_rika(a,b):
    return(a+b)
print(sa_rika(3,67))


# In[52]:


# lambda function

a = lambda x: " positive" if x+-1 ==0 else "negative"
a(-1)


# In[ ]:


#string

