#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 18:45:02 2021

@author: alivaliyev
"""

# Answer for Task-4
def stringreverse(a):
  return a[::-1]


# Answer for R-1.2
def  iseven(a):
  if (a&1)==0:
    return True
  else:
    return False

# Answer for R-1.6
def sumsq(n):
  sum=0
  for i in range(1,n,1):
    if i%2!=0:
      sum+=i*i
  return sum


# Answer for R-1.7
def sumsqu(n):
  return sum(i*i for i in range(1,n,1) if i%2!=0)
#or
def sumsq(n):
  arr=[]
  for i in range(1,n,1):
    if i%2!=0:
      arr.append(i*i)
  return sum(arr)
print(sumsq(8))

# Answer for R-1.9
for i in range(50, 90, 10):
  print(i)
  
  
  # Answer for R-1.11 
arr=[]
for i in range(0,9,1):
  arr.append(2**i)
print(arr)


# Answer for C-1.19
arr=[]
for a in range(97,123):
  arr.append(chr(a))
print(arr)


# Answer for C-1.20
def shuffle(arr):
  a=[]
  while len(a)<len(arr):
    while 1:
      i=arr[randint(0,len(arr)-1)]
      if i in a:
        i=arr[randint(0,len(arr)-1)]
      else:
        a.append(i)
        break
  return a


# Answer for C-1.28
def norm(v, p):
  sum=0
  for i in v:
   sum+=i**p
  euc = sum**(1/p)
  return euc


# Answer for P-1.35
def paradox(n):
  probab=1
  for i in range(0,n,1):
    probab*=(365-i)/365
  return 1-probab


# Answer for Task-7
def ali(l1,l2):
  while len(l1) != 0:
    l2.insert(len(l2), l1.pop(0))
  return l2
print(ali([1,2,3,4,5], [5,6,7,8]))
# Answer: While the length is not equal to 0, the code deleting the first element in l1 and adding this removed element to the end of l2.
#And this algorithm ends when the length of l1 is equal to 0.
