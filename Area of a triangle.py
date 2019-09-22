#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def insert_item(element,alist,i=0):
    '''
    OBJECTIVE: TO insert an element in a sorted list 
    Input:
    element:element to be inserted
    alist:list of numbers
    index: to keep track the position at which the element is to be inserted
    '''
    '''
    procedure: inserting element using recursion
    '''
    if (i<len(alist)):
        if(alist[i]<element):
            return insert_item(element,alist,i+1)
        else:
            alist.insert(i,element)


# In[ ]:


print("Enter your list")
input(alist)
print("Enter the element to be inserted")
input(element)
insert_item(element,alist)
print(alist)


# In[ ]:




