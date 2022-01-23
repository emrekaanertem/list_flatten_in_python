#!/usr/bin/env python
# coding: utf-8

# In[32]:


x=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
yeni = []
def duzlestir(data):
    for eleman in data:
        if type(eleman) == list:
            duzlestir(eleman)
        else:
            yeni.append(eleman)
duzlestir(x)
print(yeni)

