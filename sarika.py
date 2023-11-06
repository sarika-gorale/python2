#!/usr/bin/env python
# coding: utf-8

# In[5]:


file = open('sample.txt','r')


# In[14]:


with open('sample.txt','r') as f:
    print(f.read(15))
    


# In[12]:


with open('output.txt','w') as file:
    file.write("This is a line of text.")


# In[13]:


f.write('hello')


# In[15]:


with open('output.txt','r') as file:
    sam = file.read()
    print(sam)


# In[17]:


# append

with open('sample.txt','a') as file:
    file.write("This is an additional line.")


# In[5]:


#binary
with open('binary_data.dat','rb') as file:
    binary_data = file.read()
    print(binary_data)


# In[7]:


# binary 
with open('binary_data.dat','wb') as file:
    data = bytes([65,66,78,45,56])
    file.write(data)


# In[13]:


binary_data = b'abn_8'
text_data = binary_data.decode('utf-8')
print(text_data)


# # Exception _ handlling
# 
# 

# In[14]:


a = int(input())
b = int(input())
print(a/b)


# In[15]:


try:
    a = int(input())
    b = int(input())
    print(a/b)
    
except exception as e:
    print("KUCH TOH GALAT HAI")
    print("e.args")
    print("Please give non-zero elements")
    
else :
    print("This will execute if try block executes")
    
finally:
    print("This is always run..")


# In[17]:


# function

def main():
    print("My name is Sarika")
    
main()


# In[4]:





# In[2]:


try:
    main()
    print(j)
    
except ZeroDivisionError as e:
        print("zero se division naho hota")
        print(e.args)
        main()
        
except ValueError as e:
        print("General Error")
        print("e.args")
            
else: 
    print("this is not true")
        
finally:
        print("")
    


# In[ ]:




