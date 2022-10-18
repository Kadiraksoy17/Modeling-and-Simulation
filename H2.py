#!/usr/bin/env python
# coding: utf-8

# # Homework02: Random-Variate Generation
# ## KADİR VEYSEL AKSOY

# In[39]:


import numpy as np
import matplotlib.pyplot as plt
import math

from math import e
ln = np.log


# **Question 1:** Given the following pdf for a continuous variable, develop a generator for the variable using inverse-transform technique, generate 10000 values, and plot a histogram.
# 
# $$f(x) = \begin{cases} e^{2x}, &\quad -\infty < x \leq 0\\
#                        e^{-2x}, &\quad 0< x < \infty \\
#                        \end{cases}$$

# In[38]:


def question1(N):
    #### please write below this line
    X = []
    R = np.random.rand(N)
    for i in R:
        if i < 0.5:
            i = 0.5*ln(2*i)
        else:
            i = 0.5*ln(0.5*(1/(1-i)))
        X.append(i)
    
    #### please write above this line

    return(X)


np.random.seed(seed = 344)
X = question1(N = 10000)

print(X[0:10])
plt.hist(X)
plt.show()


# **Question 2:** Given the following cdf for a continuous variable, develop a generator for the variable using inverse-transform technique, generate 10000 values, and plot a histogram.
# 
# $$F(x) = \begin{cases} 0, &\quad x \leq -3\\
#                        \dfrac{1}{2} + \dfrac{x}{6}, &\quad -3< x \leq 0\\
#                        \dfrac{1}{2} + \dfrac{x^{2}}{32}, &\quad 0< x \leq 4\\
#                        1, &\quad x > 4
#                        \end{cases}$$

# In[118]:


def question2(N):
    #### please write below this line
    X = []
    R = np.random.rand(N)
    for i in R:
        if 0 < i <= 0.5:
            i = (6 * i) - 3
        if 0.5 < i <= 1:
            i = np.sqrt(32*i-16)
        X.append(i)
    
    
    
    
    #### please write above this line

    return(X)

np.random.seed(seed = 344)
X = question2(N = 10000)

print(X[0:10])
plt.hist(X, bins = 14)
plt.show()


# **Question 3:** The cdf of discrete random variable $X$ is given by
# 
# $$F(x) = \dfrac{x(x + 1)(2x + 1)}{n(n + 1)(2n + 1)}, \quad x = 1, 2, \dots, n.$$
# 
# When $n = 10$, develop a generator for the variable using inverse-transform technique, generate 10000 values of $X$, and plot a histogram.

# In[168]:


#I couldn't understand why I can't the results for i=1 when I try R outside from function I can get result.


def question3(N):
    #### please write below this line
    X = []
    R = np.random.rand(N)
    for i in R:
        if i <= 0.00259740259:
            i = 1
        if 0.00259740259 < i <= 0.012987:
            i = 2
        if 0.012987 < i <= 0.03636:
            i = 3
        if 0.03636 < i <= 0.077922:
            i = 4
        if 0.077922 < i <= 0.142857:
            i = 5
        if 0.142857 < i <= 0.236363:
            i = 6
        if 0.236363 < i <= 0.363636:
            i = 7
        if 0.363636 < i <= 0.5298701:
            i = 8
        if 0.5298701 < i <= 0.7402597:
            i = 9
        if 0.7402597 < i <= 1:
            i = 10
        X.append(i)
    
    
    
    #### please write above this line

    return(X)

print(X[0:10])

np.random.seed(seed = 344)
X = question3(N = 10000)

plt.hist(X, bins = np.arange(0.5, 10.5, 1))
plt.show()


# **Question 4:** For a preliminary version of a simulation model, the number of pallets $X$ to be loaded onto a truck at a loading dock was assumed to be uniformly distributed between 8 and 24. Devise a method for generating $X$, assuming that the loads on successive trucks are independent.
# 
# 
# Develop a generator for the variable using inverse-transform technique, generate 10000 values of $X$, and plot a histogram.

# In[169]:


def question4(N):
    #### please write below this line
    X=[]
    a = 7.5
    b = 24.5
    R = np.random.rand(N)
    Z = a + (b - a) * R
    for i in Z:
        i = round(i)
        X.append(i)
    #### please write above this line

    return(X)

np.random.seed(seed = 344)
X = question4(N = 10000)
print(X[0:10])
plt.hist(X, bins = np.arange(7.5, 25.5, 1))
plt.show()

