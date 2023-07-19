#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Probdistributions:
    
    # factorial
    @staticmethod
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * Probdistributions.factorial(n-1)
    
    # bernoulli distribution
    @staticmethod
    def bernoulli(p, k):
        return p**k * (1 - p)**(1 - k)
    
    
    # binomial distribution
    @staticmethod
    def binomial(n,p,x):
        return (Probdistributions.factorial(n) / 
                (Probdistributions.factorial(x) * Probdistributions.factorial(n-x))) * (p ** x) * ((1-p)**(n-x))
    
    # geometric distribution
    @staticmethod
    def geometric(p,x):
        return p * (1-p) ** x-1
    
    
    # hypergeometric distribution
    @staticmethod
    def hypergeometric(N, K, n, k):
        return (Probdistributions.comb(K,k) * Probdistributions.comb(N-k,n-k)) / Probdistributions.comb(N,n)
    @staticmethod
    def comb(n,k):
        return Probdistributions.factorial(n) / (Probdistributions.factorial(k)*Probdistributions.factorial(n-k))
    
        
    # poisson distribution
    @staticmethod
    def poisson(lmbda, k):
        return (lmbda ** k) * (2.71828 ** (-lmbda)) / Probdistributions.factorial(k)
    
    # exponential distribution
    @staticmethod
    def exponential(lmbda, x):
        result = 1
        for i in range(int(x)):
            result *= lmbda
        result *= 2.71828 ** (-lmbda * x)
        return result


# In[2]:


obj = Probdistributions()


# In[3]:


# bernoulli distribution
obj.bernoulli(0.4,0)


# In[4]:


# binomial distribution
n = 10
p = 0.5
x = range(n+1)
y = [obj.binomial(n,p,i) for i in range(n + 1)]
print(y)


# In[6]:


# geometric distribution
p = 0.5
x = range(1, 11)
y = [obj.geometric(p, i) for i in x]
print(y)


# In[7]:


# hypergeometric distribution
N = 100
K = 20
n = 10
x = range(n+1)
y = [obj.hypergeometric(N, K, n, i) for i in x]
print(y)


# In[8]:


# poisson distribution
lmbda = 4
x = range(20)
y = [obj.poisson(lmbda, i) for i in x]
print(y)


# In[9]:


# exponential distribution
lmbda = 0.5
x = [i / 10 for i in range(100)]
y = [obj.exponential(lmbda, i) for i in x]
print(y)


# In[ ]:




