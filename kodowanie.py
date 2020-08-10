#!/usr/bin/env python
# coding: utf-8

# In[4]:


s=input()
wynnik=str()
s=s+"1"
c=s[0]
i=0
for j in s:
    if c!=j:
        wynnik+=c+str(i)
        i=0
        c=j
    i+=1
print(wynnik)
    


# In[ ]:




