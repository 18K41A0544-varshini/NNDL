#!/usr/bin/env python
# coding: utf-8

# In[17]:


it=0
max_it=490
n=0.01
x=2
y=3
deltax=1
deltay=1


def der(x):
    x_der=(2*x)
    return x_der

def der(y):
    y_der=(2*y)
    return y_der

while it<max_it:
    x1=x
    y1=y
    deltax=-n*der(x1)
    deltay=-n*der(y1)
    x=x+deltax
    y=y+deltay
    it=it+1
    print("iteration",it)
    print("value is",x)
    print("value is",y)
    
    
    
print("local minimum point",x)
print("local minimum point",y)


# In[ ]:




