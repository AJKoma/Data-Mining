# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import *
from sklearn.tree import DecisionTreeClassifier

l1=pd.read_csv("D:/Rochester/Data Mining/assignment1/iris.csv",delimiter=",", usecols=(0,1,2,3,4),names=["sl","sw","pl","pw","class"])
l1.describe()
l2=l1.groupby("class")
l2=l2.agg({'sl':np.average, 'sw':np.average,'pl':np.average,'pw':np.average})
l2
#Basic statistics

ses=l1[l1['class']=='Iris-setosa']
a=ses.plot(kind="scatter",x='sl',y='sw',label='seotsa',color='red')
ves=l1[l1['class']=='Iris-versicolor']
b=ves.plot(kind="scatter",x='sl',y='sw',label='versicolor',color='blue')
vis=l1[l1['class']=='Iris-virginica']
c=vis.plot(kind="scatter",x='sl',y='sw',label='virginica',color='green')
sep=l1[l1['class']=='Iris-setosa']
d=sep.plot(kind="scatter",x='pl',y='pw',label='seotsa',color='red')
vep=l1[l1['class']=='Iris-versicolor']
e=vep.plot(kind="scatter",x='pl',y='pw',label='versicolor',color='blue')
vip=l1[l1['class']=='Iris-virginica']
f=vip.plot(kind="scatter",x='pl',y='pw',label='virginica',color='green')
#Scatter Graph

ld=cluster.KMeans(n_clusters=3,random_state=1)
lf=l1.iloc[:,1:4]
ld.fit(lf)
print (ld.labels_)
#Cluster analysis
data=np.array(l1.iloc[:,0:4])
target=np.array(ld.labels_)
train_data=np.concatenate((data[0:45, :],data[50:95, :],data[100:145, :]),axis = 0)
train_target=np.concatenate((target[0:45],target[50:95],target[100:145]),axis = 0)
test_data=np.concatenate((data[45:50, :],data[95:100, :],data[145:150, :]),axis = 0)
test_target=np.concatenate((target[45:50],target[95:100],target[145:150]),axis = 0)

clf=DecisionTreeClassifier(criterion='gini')
clf.fit(train_data, train_target)
traindata=clf.predict(train_data)
testdata=clf.predict(test_data)
sum=0
range(15)
for i in range(15):








