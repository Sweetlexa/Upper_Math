#!/usr/bin/env python
# coding: utf-8

# In[24]:


import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.linalg


# In[2]:


#Задание 1
A = np.array([[1,2,3],[4,0,6],[7,8,9]])
B = np.array([12,2,1])
np.linalg.solve(A,B)


# In[8]:


#Задание 2
A = np.array([[1,2,-1],[3,-4,0],[8,-5,2],[2,0,-5],[11,4,-7]])
B = np.array([1,7,12,7,15])
np.linalg.lstsq(A,B)


# In[23]:


#Задание 3
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([12,2,1])
# C = np.concatenate((A,B.T),axis=1)
# print(C)
# np.linalg.matrix_rank(A,0.0001)
# np.linalg.matrix_rank(C,0.0001)
np.linalg.solve(A,B) #Имеет решение


# In[25]:


#Задание 4
A = np.array([[1,2,3],[2,16,21],[4,28,73]])
P, L, U = scipy.linalg.lu(A)

print(P)
print(L)
print(U)


# In[29]:


#Задание 5 
def Q(x,y,z):
    return(x**2 + y**2 + z**2)
z = np.linspace(-1,5,201)
y = (-4 + 10*z)/21
x = -2*y + z + 1 
plt.plot(z,Q(x,y,z))
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()


# In[45]:


A = np.array([[1,2,-1],[8,-5,2]])
B = np.array([1,12])
np.linalg.lstsq(A,B)
X = np.array([ 1.38191882, -0.18081181,  0.0202952 ])
np.linalg.norm(X)


# In[33]:


z = np.linspace(-1,5,201)
y = (-4 + 10*z)/21
x = -2*y + z + 1 
plt.plot(z,x,y)
plt.xlabel('x')
plt.xlim(0,2)
plt.ylabel('y')
plt.grid(True)
plt.show()


# In[42]:


#Задание 6
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([2,5,11])
Q, R = np.linalg.qr(A)
print(R)
print(Q)
R1 = R[:2, :2]
print(R1)
B1 = np.dot(np.transpose(Q), B)[:2]
print(B1)
X1 = np.linalg.solve(R1, B1)
print(X1)
X = np.append(X1, 0)
print(X)
np.linalg.norm(X)


# In[41]:


np.linalg.norm(np.dot(A,X) - B) #Норма вектора невязки исходной ЛСУ (одно из псевдорешений)


# In[43]:


A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([2,5,11])
np.linalg.lstsq(A,B)


# In[44]:


X = np.array([1.25,  0.5 , -0.25])
np.linalg.norm(X) # Псевдорешение, обладающее минимальньной нормой - нормальное псевдорешение


# In[ ]:




