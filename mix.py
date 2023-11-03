#!/usr/bin/env python
# coding: utf-8

# In[1]:


fruits =['banana','apple','cherry','mango']

sorted_fruits =sorted(fruits, key=lambda x: x.lower())
print(sorted_fruits)


# In[19]:


def count_fruits(basket):
    if  basket:
    else:
        return 1 + count_fruits(basket[1:])
    
basket = ['apple','banana','orange','mango','kiwi']

num_fruits = count_fruit(basket)

print(f"There are {num_fruits} fruits in the basket.")


# In[31]:


def multiplay_rectangle_area (length, width):
    area = length * width
    return area 

#INPUT VALUES
length = 9

width = 9

#call the fuction and store the result
area_of_rectangel = calculate_rectangle_area(length, width)

#Print the result

print(f"The area of rectangle with length {width} and width {length} is: {area_of_rectangle}")


# In[7]:


def calculate_rectangle_area (length, width):
    area = length * width
    return area 

#INPUT VALUES
length = 9
width = 9

#call the fuction and store the result
area_of_rectangle = calculate_rectangle_area(length, width)

#Print the result
print(f"The area of rectangle with length {length} and width {width} is: {area_of_rectangle}")


# In[ ]:





# In[ ]:




