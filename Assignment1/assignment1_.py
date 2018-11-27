# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
np.set_printoptions(threshold=np.nan)

l1=pd.read_csv("D:/Rochester/Data Mining/assignment1/iris.csv",delimiter=",", usecols=(0,1,2,3,4),names=["sedal length in cm","sedal width in cm","petal length in cm","petal width in cm","class"])
l1.describe()
l2=l1.groupby("class")
l2=l2.agg({'sedal length in cm':np.average, 'sedal width in cm':np.average,'petal length in cm':np.average,'petal width in cm':np.average})


l3=l2.T
l2
l3
l2.plot(kind="bar")
plot=l3.plot(kind="bar")


ses=l1[l1['class']=='Iris-setosa']
ves=l1[l1['class']=='Iris-versicolor']
sep=l1[l1['class']=='Iris-setosa']
vep=l1[l1['class']=='Iris-versicolor']
vis=l1[l1['class']=='Iris-virginica']
vip=l1[l1['class']=='Iris-virginica']

target=np.array(l1['class'])
target
sl=np.array(l1['sedal length in cm'])
sw=np.array(l1['sedal width in cm'])
pl=np.array(l1['petal length in cm'])
sw=np.array(l1['petal width in cm'])


#Basic statistics
plt.figure()
ses=l1[l1['class']=='Iris-setosa']
a=plt.scatter(ses['sedal length in cm'],ses['sedal width in cm'],label='setosa',color='red')
ves=l1[l1['class']=='Iris-versicolor']
b=plt.scatter(ves['sedal length in cm'],ves['sedal width in cm'],label='versicolor',color='blue')
vis=l1[l1['class']=='Iris-virginica']
c=plt.scatter(vis['sedal length in cm'],vis['sedal width in cm'],label='virginica',color='green')
plt.title('Plot of sepal length vs sepal width')
plt.xlabel('sepal length in cm')
plt.ylabel('sepal width in cm')
plt.legend((a,b,c),['setosa', 'versicolor','virginica'])
plt.show()

plt.figure()
sep=l1[l1['class']=='Iris-setosa']
d=plt.scatter(ses['petal length in cm'],ses['petal width in cm'],label='setosa',color='red')
vep=l1[l1['class']=='Iris-versicolor']
e=plt.scatter(ves['petal length in cm'],ves['petal width in cm'],label='versicolor',color='blue')
vip=l1[l1['class']=='Iris-virginica']
f=plt.scatter(vis['petal length in cm'],vis['petal width in cm'],label='virginica',color='green')
plt.xlabel('petal length in cm')
plt.ylabel('petal width in cm')
plt.legend((a,b,c),['setosa', 'versicolor','virginica'])
plt.title('Plot of petal length vs spetal width')
plt.show()



#Scatter Graph







