
# coding: utf-8

# In[112]:


def insert_item(element,alist,i = 0):
    '''
    OBJECTIVE: To insert a given element into a sorted list of numbers so that the list remains sorted 
    INPUT : 
        element: The element to be inserted, 
        alist: The sorted list of numbers,
        i    : to keep track the position of insertion
    OUTPUT : the list with inserted element 
    
    '''
    '''
    PROCEDURE: To insert the element using recursion 
    '''

    if(len(alist))==i:    
        alist.insert(i,element)
    elif(alist[i]<element):
        return insert_item(element,alist,i+1)
    else:
        alist.insert(i,element)
    


# In[113]:


alist=[10,30,40]
insert_item(25,alist,0)
print(alist)


# In[116]:


def sort_list(alist,i=0):
    '''
    OBJECTIVE: To insert a given element into a sorted list of numbers so that the list remains sorted 
    INPUT : The element to be inserted, ele 
    The sorted list of numbers,alist
    OUTPUT : the list with inserted element 
    '''
    '''
    PROCEDURE: To insert the element using recursion 
    '''
    if(i<len(alist)): 
        if(alist[i]<alist[i+1]):
            return sort_list(alist,i+1)
    else:
        temp=alist[i]
        alist[i]=alist[i+1]
        alist[i+1]=temp
        return sort_list(alist,i+1)
    print(alist)


# In[117]:


alist=[10,30,15,45,35]
sort_list(alist)

