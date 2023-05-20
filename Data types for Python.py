#!/usr/bin/env python
# coding: utf-8

# In[7]:


Different data types used in python.
Like we have string data, numeric data, alphanumeric, bits data 0,1 or True, False. 


# In[ ]:


String data like name or anything that is written in quotation marks. "Earth"
Numeric data is written without the quotation marks. 123, 456, etc. 
int (interger type data) just like 1,2,3,4... 

float is used for the decimal point value. To add the decimal value. Like 1.25, 2.5,3.6 etc.

complex is used for complex number which are written in a+bj. In compelx we have two different
parts. One is real number and ther is complex. Here a is real part and b is complex part.  


# In[11]:


x = 5
y = 2
z = 3.5
country_name = "USA" 
z1 = "123"
y1 = 123456789.123456789
print(type(x))
print(type(y))
print(type(z))    
print(type(country_name))
print(type(z1))
print(type(y1))


# In[13]:


complex_data_type = 1+5j
print(type(complex_data_type))
j is denoated for the cmplex number. We can not add real and complex number. We can only add real
to real number and complex to complex number. 


# In[16]:


complex_number_1 = 1+5j
complex_number_2 = 2+4j
add = complex_number_1 + complex_number_2
print(add)
print(type(add))
mul = complex_number_1 * complex_number_2
print(mul)
Boolean data type in which we have two vlaues True and False.


# In[20]:


x = True
y = False
print(type(x))
print(type(y))


# In[ ]:


For the sequence data type two important data types are used.
1. List 
2. Tuple


# In[36]:


Country_names = ["Pakistan","India", "United Kingdom", "USA","Russia", "China","France"]
length = len(Country_names)
print(length)
index = length - 1
print("length is"+str(length))


# In[ ]:




