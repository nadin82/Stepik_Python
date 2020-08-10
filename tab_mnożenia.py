#!/usr/bin/env python
# coding: utf-8

# In[8]:


a=int(input())
b=int(input())
c=int(input())
d=int(input())
for i in range(c,d+1):
    print('\t', i, end='')
print()
for j in range(a, b+1):
    print (j, end='')
    for i in range(c, d+1):
        print('\t', i*j, end='')
    print()


# In[ ]:




