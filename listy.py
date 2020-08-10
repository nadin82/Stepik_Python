#!/usr/bin/env python
# coding: utf-8

# In[18]:


lista=[int(i) for i in input().split()]
wyn=[]
j=0
for i, item in enumerate(lista):
    if lista.count(item)>1 and item not in wyn:
        wyn.insert(j, item)
        j+=1
for k in wyn:
    print(k, end=' ')


# In[ ]:




