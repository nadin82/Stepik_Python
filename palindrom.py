#!/usr/bin/env python
# coding: utf-8

# In[2]:


s=input()
i=0
j=len(s)-1
is_palindrom=True
while i<j:
    if s[i]!=s[j]:
        is_palindrom=False
        break
    i+=1
    j-=1
if is_palindrom:
    print('Yes')
else:
    print('No')


# In[ ]:




