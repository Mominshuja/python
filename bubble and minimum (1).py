
# coding: utf-8

# In[91]:


def bubble(alist,i,f):
    '''
    Objective: To bubble the least element of list at the end in a given range 
    Input: alist: The unsorted list
           i: starting index 
           f: end index
    output: The sorted list
    Side Effect: none

    '''
    '''
    Approach: Using Recursion
    '''
    if(i<f):
        if(alist[i]<alist[i+1]):
            temp=alist[i]
            alist[i]=alist[i+1]
            alist[i+1]=temp
        return bubble(alist,i+1,f)
    return alist
    


# In[94]:


alist=[10,5,20,70,50]
bubble(alist,0,3)


# In[121]:


def minimum(alist,i,f):
    '''
    Objective: To find the least element of list in a given range 
    Input: alist: The unsorted list
           i: starting index 
           f: end index
    output: The index of the Minimum element of the list in a given range
    Side Effect: none

    '''
    '''
    Approach: Using Recursion
    '''
    temp=i
    if(i<f):
        if(alist[i+1]<alist[temp]):
            temp= i+1
            return minimum(alist,temp,f)
    return temp
        


# In[126]:


alist=[90,30,20,10,50]
minimum(alist,0,2)

