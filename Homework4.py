#!/usr/bin/env python
# coding: utf-8

# In[29]:


mu = 0
sigma = 2
x = 1

yafi = 1 / (sigma * math.sqrt(2 * math.pi))
exponential = math.exp(-0.5 * ((x - mu) / sigma) ** 2)

result = yafi * exponential

print(result)


# In[28]:


def is_even(num): 
    return num % 2 == 0
is_even(4)


# In[36]:


def isPrime_for(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def getNumPrimes_for(n):
    count = 0
    for i in range(2, n):
        if isPrime_for(i):
            count += 1
    return count


n = int(input("Enter an integer number: "))
num_primes = getNumPrimes_for(n)
print(f"There are {num_primes} prime numbers smaller than {n}.")


# In[ ]:


B. Juyptter notebook is faster


# In[ ]:




