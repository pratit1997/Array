#!/usr/bin/env python
# coding: utf-8

# In[15]:


def find_missing_number(x,n):
    
    expected_total=n*(n+1)//2
    print(expected_total)
    actual_total=sum(x)
    return expected_total-actual_total
    



Array = [1,2,3,4,7]
n=len(Array)+1

missing_number=find_missing_number(Array,n)
print(missing_number)


# In[ ]:




