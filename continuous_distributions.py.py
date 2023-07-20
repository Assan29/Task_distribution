#!/usr/bin/env python
# coding: utf-8

# In[5]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[6]:


def distribution():
    
    list_dist = ['normal','geometric','hypergeometric','poisson','binomial','exponential','chi_squared','uniform','lognormal']
    x = np.random.choice(list_dist)
    

    
    if x ==  'normal':
        y = np.random.normal(0, 1, 1000)
    elif x == 'geometric':
        y = np.random.geometric(0.2,1000)
    elif x == 'hypergeometric':
        y = np.random.hypergeometric(500, 500, 20, 1000)
    elif x == 'poisson':
        y = np.random.poisson(5, 1000)
    elif x == 'binomial':
        y = np.random.binomial(10, 0.5, 1000)
    elif x == 'exponential':
        y = np.random.exponential(1, 1000)
    elif x == 'chi_squared':
        y = np.random.chisquare(2, 1000)
    elif x == 'uniform':
        y = np.random.uniform(-1, 1, 1000)  
    else:
        y = np.random.lognormal(1,0.5,1000)
        
        
    
    print(f'p_mean     : {np.mean(y)}')
    print(f'p_variance : {np.var(y)}')
    print(f'p_std      : {np.std(y)}')
        
    sns.histplot(y, kde=True)
    plt.title(f'{x} Distribution')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.show()
    
    
    num_sample = 499
    print(f'No.of samples : {num_sample}')
    
    sample_size = 50
    print(f'samples size  : {sample_size}')
    
    sample = []
    for i in range(num_sample):
        z = np.random.choice(y,sample_size)
        sample.append(np.mean(z))
    
    sns.histplot(sample, kde=True)
    plt.title(f'{x} sample_distribution')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.show()
    
    
    print(f's_mean        : {np.mean(sample)}')
    print(f's_variance    : {np.var(sample)}')
    print(f's_std         : {np.std(sample)}')
    print(f'satnded_error : {np.std(sample) / np.sqrt(sample_size)}')
    
    
distribution()


# In[ ]:




