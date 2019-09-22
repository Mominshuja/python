#!/usr/bin/env python
# coding: utf-8

# In[30]:


def rtarea(b,h):
    area=(b*h)/2
    return(area)
def oarea(a,b,c):
    s=((a+b+c)/2)
    area=((s*(s-a)*(s-b)*(s-c))**0.5)
    return(area)
'''
OBJECTIVE: To find the area of triangle
INPUT    : The type of triangle(right angeled or any other)
           The sides of the triangle(a,b,c)
           The Altitude or height(h)
OUTPUT   : The area of the given triangle
'''
'''
Approach :For Right-Angeled Triangle Using Formula Area=(base*height)/2
          For any other using FormulaArea=(s(s-a)(s-b)(s-c))^0.5
'''
print("choose the input type\n1) Base and Height \n2) sides of Triangle")
k = input()
if(k == '1'):
    print("Enter The Base And Height")
    b=input()
    h=input()
    b=float(b)
    h=float(h)
    print(rtarea(b,h))
if k == '2':
    print("Enter the sides of Triangle")
    a=input()
    b=input()
    c=input()
    a=float(a)
    b=float(b)
    c=float(c)
    print("Area=",oarea(a,b,c))

else:
    print("Wrong choice")
    
           


# #### 

# In[ ]:




