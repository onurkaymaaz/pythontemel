#!/usr/bin/env python
# coding: utf-8

# In[1]:


l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
nl = []
def flatten(n):
    for i in n :
        if isinstance(i,list):
            flatten(i)
        else:
            nl.append(i)

flatten(l)
print(nl)


# In[ ]:





# In[ ]:




