#!/usr/bin/env python
# coding: utf-8

# In[1]:


#user-defined funcction:
def f1():              #stage1:defining the function
    print("hi")
f1()                   #stage2:calling a function.


# In[8]:


def f2():
    x=input(int())
    y=input(int())
    print(x+y)
f2()    


# In[12]:


def sum1():
    num1=int(input())
    num2=int(input())
    print(num1+num2)


# In[13]:


sum1()


# In[14]:


sum1()


# In[16]:


#parameters and arguments:
def sum1(x,y):   #parameter
    print(x+y)


# In[20]:


sum1(1,2)     #argument


# In[19]:


sum1(12,11)


# In[23]:


def sum2(x1,x2,x3,x4,x5):   #parameter
    print(x1+x2+x3+x4+x5)


# In[24]:


sum2(11,22,33,44,55)    #argument


# In[25]:


def sum3(x1,x2,x3,x4,x5=10):   # default parameter
    print(x1+x2+x3+x4+x5)


# In[27]:


sum3(1,2,3,4)


# In[30]:


def sum4(x=1,y=2,z=3):
    print(x+y+z)


# In[29]:


sum4()      #default parameter


# In[36]:


def sum4(x=1,y=2,z=3):
    print(x+y+z)


# In[37]:


sum4(2,2,3)


# In[52]:


def bio_data(name,age,height):
    """this function prints your bio_data"""    #doc string(documentation string)
    print("My name is {}".format(name))
    print("My age is {}".format(age))
    print("My height is {}".format(height))


# In[50]:


bio_data("hemanth",22,186.3)   #positional argument:


# In[51]:


bio_data(age=23,name="hemanth",height=186.2)     #keyword argument


# In[54]:


bio_data.__doc__


# In[55]:


print.__doc__


# In[1]:


#create a calculator function:
def calculator():
    oper="a"
    while oper!="c":
        number=int(input('first number')) 
        oper=input('type any of +,-,/,*,,type c to exit')
        number1=int(input('second number'))
        if oper=="+":
            print('{}+{}={}'.format(number,number1,number+number1))
        elif oper=="-":
            print('{}-{}={}'.format(number,number1,number-number1))
        elif oper=="*":
            print('{}*{}={}'.format(number,number1,number*number1))
        elif oper=="c":
            break
        else:
            print('oper not found')
    


# In[ ]:


calculator()


# In[ ]:





# In[ ]:




