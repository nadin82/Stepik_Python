#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def update_dictionary(d, key, value):
    if d.get(key)!=None:
        d[key]+=[value]
    else: 
        if d.get(2*key)!=None:
            d[2*key]+=[value]
        else:
            d[2*key]=[value]

#d = {}
#print(update_dictionary(d, 1, -1))  # None
#print(d)                            # {2: [-1]}
#update_dictionary(d, 2, -2)
#print(d)                            # {2: [-1, -2]}
#update_dictionary(d, 1, -3)
#print(d)                            # {2: [-1, -2, -3]}


# In[ ]:


lista=[str(i) for i in input().split()]
for i in range(len(lista)):
    lista[i]=lista[i].lower()
d={}
while lista!=[]:
    n = lista.count(lista[0])
    d[lista[0]] = n
    x=lista[0]
    for i in range(n):
        lista.remove(x)
for key, value in d.items():
    print(key, value)

#Sample Input 1:
#a aa abC aa ac abc bcd a
#Sample Output 1:
#ac 1
#a 2
#abc 2
#bcd 1
#aa 2


# In[ ]:


n=int(input())
d=dict()
lista=[]
for i in range(n):
    x=int(input())
    lista.append(x)
    if d.get(x)==None:
        d[x]=f(x)
for x in lista:
    print(d[x])

#Sample Input:
#5
#5
#12
#9
#20
#12
#Sample Output:
#11
#41
#47
#61
#41    

