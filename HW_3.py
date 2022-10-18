#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Занятие 3. Задание 1.
get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
import math 
import numpy as np
k = 3
a = 0.1
b = 2
x = np.linspace(0,3*np.pi,201)
y = k * np.cos(x-a) + b 
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()


# In[28]:


#Задание 3.2
x = np.linspace(0,np.pi,2001)
R = 2
y = R*np.sin(x)
plt.polar(x,y)


# In[44]:


x = np.linspace(-2,3,201)
plt.plot(x, (-1 + np.exp(x)+x)/x)
plt.plot(x, x**2-1)
plt.ylim(-1,5)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()


# In[45]:


from scipy.optimize import fsolve
def e(p):
    x,y = p
    return (y - x ** 2 + 1,np.exp(x)+x*(1-y)-1)
x1,y1 = fsolve(e,(-2,1))

print(x1,y1)


# In[ ]:




