#!/usr/bin/env python
# coding: utf-8

# # TASK 1 AND TASK 2

# In[1]:


import math


# In[2]:


x = 0
y = 1

print(x)
print(y)

x = x + 3
y = y + x

print(x)
print(y)


# In[3]:


x = 1 + 1 * 2
y = (1 + 1) * 2
z = 1 + ( 1 * 2 )
a =  1 + 1 * 2 / 2
b =  (1 + 1 * 2 ) /  2


# In[4]:


print(x)
print(y)
print(z)
print(a)
print(b)


# # TASK 3 and task 4

# In[5]:


def number_65(a,b):
    if ((a==65) or (b==65)):
        return True
    if ((a + b)==65):
        return True
    else:
        return False
    
a = int(input('Enter number one : '))
b = int(input('Enter number two : '))

number_65(a,b)


# In[6]:


def number_3(x,y):
    if (x==3 or y==3):
        return True
    elif '3' in str(x + y):
        return True
    else:
        return False
    
x = int(input('Enter number  : '))
y = int(input('Enter number  : '))

number_3(x,y)


# # Task 5 and task 6

# In[7]:


def Area(a,b,c):  
  
    if (a < 0 or b < 0 or c < 0 or (a+b <= c) or (a+c <=b) or (b+c <=a) ):  
        print('Not valid')  
        return
           
    s = (a + b + c) / 2
      
    # calculate the area  
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    print('The Area is %f' %area)  
  


# In[8]:


def max_two( x, y ):
    if x > y:
        return x
    return y
## max of 3
def max_of( x, y, z ):
    return max_two( x, max_two( y, z ) )


# In[9]:


print(max_of(24,22,1000))


# # Task 7 and task 8

# In[10]:


temperature = input("Enter the  temperature you: ")
degree = int(temperature[:-1])
i_convention = temperature[-1]

if i_convention.upper() == "C":
  result = int(round((9 * degree) / 5 + 32))
  i_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = int(round((degree - 32) * 5 / 9))
  i_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in", i_convention, "is", result, "degrees.")


# In[11]:


import datetime 
  
def num_time(n): 
    return str(datetime.timedelta(minutes = n))


# In[12]:


n = 133
print(num_time(n))


# # Task 9,10, and 11

# In[13]:


[i for i in range(1000) if i % 3 == 0 or i % 5 == 0]


# In[14]:


sent = input('Enter your word: ')

for vowel in 'A,E,I,U,O,a,i,e,o,u':
    if vowel in sent:
        print(vowel)


# In[15]:


string1 = 'cars'
string2 = 'carbon'

s1 = set(string1)
s2 = set(string2)

common_char = s1 & s2

print(common_char)


# In[16]:


pip install git-clone


# In[ ]:




