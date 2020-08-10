#!/usr/bin/env python
# coding: utf-8

# In[29]:


a=float(input('Pierwsza liczba'))
b=float(input('Druga liczba'))
c=input('działanie')
if b==0 and (c=="/" or c=="mod" or c=="div"):
    print('Dzielenie przez 0!')
else:
    if c=="+":
        print(a+b)
    elif c=="-":
        print(a-b)
    elif c=="/":
        print(a/b)
    elif c=="*":
        print(a*b)
    elif c=="mod":
        print(a%b)
    elif c=="pow":
        print(a**b)
    elif c=="div":
        print(a//b)
    else:
        print("некорректно введена операция")


# In[ ]:





# In[ ]:




