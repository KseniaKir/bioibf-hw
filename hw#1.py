#!/usr/bin/env python
# coding: utf-8

# Написать программу, принимающую числа𝑎, 𝑏, 𝑐и решающуюквадратное уравнение 𝑎𝑥2+𝑏𝑥+𝑐= 0. Все особые случаидолжны быть разобраны. Результат может быть выведен наэкран в произвольном виде.

# In[4]:


a = int(input("Input a "))
b = int(input("Input b "))
c = int(input("Input c "))


# In[5]:


D = b**2 - 4*a*c
x1 = (-b+D**(1/2))/2
x2 = (-b-D**(1/2))/2


# In[6]:


print (x1, x2)


# Ввести список чисел (не обязательно целых), посчитать их среднее арифметическое.

# In[7]:


list = [2, 2.4, 5, 6, 2]
sum = 0
n = len(list)
for i in range (n):
    sum += list[i]
print ("Mean = ", sum/n)


# Ввести список чисел (не обязательно целых), вывести его вобратном порядке.

# In[8]:


list = [2, 2.4, 5, 6, 2]
print (list[::-1])


# Вводится число 𝑛, затем по одному вводятся 𝑛 чисел (необязательно целых). Не сохраняя числа в список, найти максимальное из них.

# In[9]:


n = int(input("Number of numbers: "))
a = int(input())
maxx = a
for i in range (n-1):
    a = int(input())
    if a>maxx:
        maxx = a
print ("Your maximum is: ", maxx)


# Вводится число 𝑛, затем по одному вводятся 𝑛 чисел (необязательно целых). Не сохраняя числа в список, найти второй максимум (предпоследнее число при выстраивании по возрастанию).

# In[10]:


n = int(input("Number of numbers: "))
max1 = int(input())
max2 = int(input())
if max2>max1:
    a = max1
    max1 = max2
    max2 = a
if n>2:
    for i in range (n-2):
        num = int(input())
        if (max2 < num) and (num < max1):
            max2 = num
print ("Second maximum is: ", max2)


# In[ ]:




