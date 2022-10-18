#!/usr/bin/env python
# coding: utf-8

# In[82]:


#Тема 2.Задание 2.
get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
import math 
import numpy as np
x = np.linspace(-10,10,10)
y = x+1
y1 = -1/1*x+1
plt.plot(x,y)
plt.plot(x,y1)
plt.xlabel('x')
plt.ylabel('y')


# In[76]:


#Тема 2. Задание 3.
# Эллипс 
t = np.linspace( 0 , 2 * np.pi , 150 )
 
R = 1
 
x = R * np.cos( t )
y = R * np.sin( t )
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')


# In[78]:


#Тема 2. Задание 3.
# Окружность 
import numpy as np
import matplotlib.pyplot as plt
 
theta = np.linspace( 0 , 2 * np.pi , 150 )
 
radius = 0.4
 
a = radius * np.cos( theta )
b = radius * np.sin( theta )
 
figure, axes = plt.subplots( 1 )
 
axes.plot( a, b )
axes.set_aspect( 1 )
 
plt.show()


# In[ ]:





# In[74]:


#Тема 2. Задание 3.
# Эллипс через каноническое уравнение (но не получилось вывести картинку)
x = []
y1 = []
y2 = []
a = 0.1
b = 0.01
for i in range(100):
    x_ = i/100
    x.append(x_)
    y1.append(math.sqrt((1-x_**2/a**2)/b**2))
    y2.append(-math.sqrt((1-x_**2/a**2)/b**2))
plt.xlim(0,100)
plt.plot(x,y1)
plt.plot(x,y2)
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# In[81]:


#Тема 2. Задание 5.
#Параллельные плоскости 
from pylab import * 
from mpl_toolkits.mplot3d import Axes3D
fig = figure()
ax = Axes3D(fig)
X = np.arange(-5,5,0.5)
Y = np.arange(-5,5,0.5)
X,Y = np.meshgrid(X,Y)
Z1 = 2*X + 5 * Y
Z2 = 2*X + 5*Y + 5
ax.plot_surface(X,Y,Z1)
ax.plot_surface(X,Y,Z2)
show()


# In[83]:


#Тема 2. Задание 5.
#Трехмерный график плоскости второго порядка 
from pylab import * 
from mpl_toolkits.mplot3d import Axes3D
fig = figure()
ax = Axes3D(fig)
X = np.arange(-5,5,0.5)
Y = np.arange(-5,5,0.5)
X,Y = np.meshgrid(X,Y)
Z = 2*X**2 + 5 * Y**2
ax.plot_surface(X,Y,Z)
show()


# In[84]:


#Тема 2. Задание 5.
#Трехмерный график плоскости второго порядка 
from pylab import * 
from mpl_toolkits.mplot3d import Axes3D
fig = figure()
ax = Axes3D(fig)
X = np.arange(-5,5,0.5)
Y = np.arange(-5,5,0.5)
X,Y = np.meshgrid(X,Y)
Z = 2*X**2/4 - Y**2/10
ax.plot_surface(X,Y,Z)
show()


# In[ ]:




