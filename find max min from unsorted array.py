#!/usr/bin/env python
# coding: utf-8

# In[6]:


def find_Largest(x):
    n=len(x)
    largest=x[0]
    smallest=x[0]
    for i in x:
        if i>largest:
            largest=i
        elif i<smallest:
            smallest=i
    return largest,smallest


array=[6,2,7,9,4,6,3,6,3]
output=find_Largest(array)
print(output)


# In[ ]:




