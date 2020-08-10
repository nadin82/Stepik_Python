#!/usr/bin/env python
# coding: utf-8

# In[5]:


F=input()
if F=='треугольник':
    a=float(input())
    b=float(input())
    c=float(input())
    p=(a+b+c)/2
    S=(p*(p-a)*(p-b)*(p-c))**0.5
    print(S)
elif F=='прямоугольник':
    a=float(input())
    b=float(input())
    S=a*b
    print(S)
elif F=='круг':
    r=float(input())
    S=3.14*(r**2)
    print(S)
else:
    print('неправильно введено тип фигуры комнаты')


# In[ ]:





# In[ ]:




