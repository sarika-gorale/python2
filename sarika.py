#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello world")


# In[2]:


def sarika_01 (f,d):
    return f / d
result=sarika_01 (6, 3)
print(result)


# In[4]:


def add(a,b):
    return(a+b)
print(add(10,20))


# In[5]:


def mul(a,g):
    return(a * g)
print(mul(4,6))


# In[12]:


def calculaate_square_area(side, side):
    area = side * side
    return area

side = 5
side = 5

area_of_square = calculate_square_area(side,side)
print(f"The area of the square with side {side} is : {area_of_sqquare} ")


# In[18]:


#lambda function
b = lambda x:"prime" if x/2+1 == 0 else "not prime"
b(10)


# In[23]:


a = lambda x: " positive" if x+-1 ==0 else "negative"
a(-1)


# In[26]:


# string
my_string = "Hello World"
print(my_string)

a= " my world"
print(a.upper())
# In[27]:


a= " my world"
print(a.upper())


# In[29]:


a= " my world"
print(a.lower())


# In[33]:


a= " my   world"
print(a.strip())


# In[36]:


a= " my world"
print(a.replace("w","M"))


# In[37]:


a= " my world"
print(a.split())


# In[38]:


a= " my world"
print(a[5])


# In[5]:


# formatted
name = input("Enter your Name")
age = int(input("Enter your age"))

formatting_string =f"my name is {name} and i am {age} year old."
print(formatting_string)


# In[7]:


# list datatype

# creating list

s=['sam', 'sona', 'hash']

print(s)


# In[8]:


# indexing

s=['sam', 'sona', 'hash']
 
print(s[1])

print(s[-1])


# In[19]:


# slicing

s=['sam', 'sona', 'hash']

print(s[0:2])


# In[22]:


# list methods

# pop method

no = [2,4,3,6,8,0,8]
no.pop(0)
print(no)


# In[30]:


# delet method

no = [2,4,3,6,8,0,8]
del no
print(no)


# In[31]:


# clear method

no = [2,4,3,6,8,0,8]
no.clear()
print(no)


# In[32]:


#remove method

no = [2,4,3,6,8,0,8]
no.remove(4)
print(no)


# In[34]:


# slicing method

no = [2,4,3,6,8,0,8]
no = no[:1] + no [3:]
print(no)


# In[35]:


# comprehnsion

no = [2,4,3,6,8,0,8]
no = [x for x in no if x != 2]
print(no)


# In[1]:


# tuple

t1 = (1,2,3,4,5)

print(t1)
print(type(t1))



# In[2]:


# Indexing

t1 = (1,2,3,4,5)

print(t1[2])


# In[3]:


t4 = (1,2,3, True ,(1,2,3))
print(t4)


# In[7]:


# type conversion
t2 = tuple('sarika')
print(t2)


# In[11]:


# operators

# arithemetic operator

t1 = (1,2,3,4,5)
t2 = (6,7,8,9,0)

print(t1 + t2)
print(t1 * 2)


# In[17]:


# operations

# arithemetic operators

t1 = (1,2,3,4,5)
t2 = (6,7,8,9,0)

mul = t1 * 2
add = t1 + t2
print(add)
print(mul)



# In[19]:


# comparison operator

t1 = (1,2,3,4,5)
t2 = (6,7,8,9,0)

equality = t1 == t2
inequality = t1 != t2
greater_than = t1 > t2
less_than = t1 < t2
greater_than_equal_to = t1 >= t2
less_than_equal_to = t1 <= t2
print(equality)
print(inequality)
print(equality)
print(greater_than)
print(less_than)
print(greater_than_equal_to)
print(greater_than_equal_to)


# In[20]:


# membership operator

t1 = (1,2,3,4,5)
t2 = (6,7,8,9,0)

print(1 in t1)
print(7 not in t2)


# In[22]:


# slice operator 
   

t1 = (1,2,3,4,5)
t2 = (6,7,8,9,0) 

print(t1[2:5])


# In[23]:


# comma creator

c = 1,2,3
print(c)


# In[27]:


# tuple functions

# len

t1 = (1,2,3,4)

print(len(t1))

# sum

print(sum(t1))

#min

print(min(t1))

# min

print(max(t1))

# sorted

print(sorted(t1,reverse=True))


# In[1]:


# Dictionary


s = {'name' : 'hashu', 'age' : '22', 'village' : 'bhokari'}
print(s)


# In[2]:


# dictionary methods

# 1) clear()


s = {'name' : 'hashu', 'age' : '22', 'village' : 'bhokari'}
s.clear()
print(s)


# In[5]:


# 2) copy()
s = {'name' : 'hashu', 'age' : '22', 'village' : 'bhokari'}
a = s.copy()
print(a)


# In[6]:


# 3) items()


s = {'name' : 'hashu', 'age' : '22', 'village' : 'bhokari'}
print(s.items())


# In[7]:


# 4) keys()


s = {'name' : 'hashu', 'age' : '22', 'village' : 'bhokari'}
print(s.keys())


# In[8]:


# 5) values()

s = {'name' : 'hashu', 'age' : '22', 'village' : 'bhokari'}
print(s.values())


# In[10]:


# 6) get(key[,default])


s = {'name' : 'hashu', 'age' : '22', 'village' : 'bhokari'}
print(s.get('name'))
print(s.get('age'))
print(s.get('village'))


# In[12]:


# 7) pop(key[,default])

s = {'name' : 'hashu', 'age' : '22', 'village' : 'bhokari'}
print(s.pop('name'))
print(s)


# In[14]:


# 8) popitem()

s = {'name' : 'hashu', 'age' : '22', 'village' : 'bhokari'}
item = s.popitem()
print(item)
print(s)


# In[16]:


# problem : create a dictionary with number as keys and their squares as values.

squares = {}
for num in range(5,11):
    squares[num]= num**2
print(squares)


# In[17]:


# problem : create a dictionary with number as keys and their squares as value.
# using dictionary comprehensation :
squares = {num : num ** 2 for num in range(3,8)}
print(squares)


# In[18]:


# using if condition
products = {'phone': 20, 'laptop' :90, 'charger': 35, 'ipad': 67, 'headphone': 45}
{key:value for (key,value) in products.items() if value > 35}


# In[20]:


# nested comprehensation 
 # print tables of number from 2 to 5
    
{i:{j:i*j for j in range(1,11)} for i in range(2,6)}


# In[ ]:




