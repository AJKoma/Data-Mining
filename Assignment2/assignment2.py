# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 18:20:32 2017

@author: AJKoma
"""

import numpy as np
import pandas as pd
l1=pd.read_csv("D:/Rochester/Data Mining/assignment2/data1.csv",delimiter=",",names=["num"],dtype=str)
print(l1["num"])
l2={}
for i in range(len(l1)):
    c=l1["num"][i]
    l2[c]=l2.get(c,0)+1;
print(l2)
l3=sorted(l2.items(), key=lambda d :d[1], reverse = False)
print(l3)
# Result for (a)

b1=pd.read_csv("D:/Rochester/Data Mining/assignment2/data2.csv",delimiter=",",names=["num"],dtype=int)
len(b1)
def wid(a):
  b=(1/a*b1['num'])
  l4={}
  print(b)
  for j in range(len(b1)):
      b[j]=int(b[j])    
  for i in range(len(b1)):
      c=b[i]
      print(c)
      l4[c]=b.get(c,0)+1;
      l4
      l5=sorted(l4.items(), key=lambda d :d[1],reverse = False)
      print(l5)
  return l5

wid(5)
#Result for (b). Results in form of (a,b), a is the level and b is the frequency.

c1=pd.read_csv("D:/Rochester/Data Mining/assignment2/data2.csv",delimiter=",",names=["num"],dtype=int)
c2=c1.sort_values(by='num')
len(c1)
c3=np.array(c2)
c3
def binnumber(n):
    m=int(len(c1)/n)   
    for i in range(0,len(c1),m):
       c4=c3[i:i+m]
       print(c4)       
    return
binnumber(7)
#Result for (c)
