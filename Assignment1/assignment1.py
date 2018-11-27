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
np.set_printoptions(threshold=np.nan)

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
lf=l1.iloc[:,0:4]
ld.fit(lf)
print (ld.labels_)
ld.labels_
cluster=np.array(ld.labels_)
b=np.zeros(150,dtype=int)
b.shape
target=np.array(l1['class'])
for i in range(150):
    if target[i]=='Iris-setosa' :
        b[i]=1
    if target[i]=='Iris-versicolor':
        b[i]=0
    if target[i]=='Iris-virginica':
        b[i]=2
print(b)
sum=0
for i in range(150):
    if cluster[i]==b[i]:
        sum=sum+1
        sum
print('cluster analysis accuracy=',sum*100/150,'%')
#Cluster analysis

data=np.array(l1.iloc[:,0:4])
target=np.array(l1['class'])
train_data,test_data,train_target,test_target=cross_validation.train_test_split(data,target,test_size=0.3,random_state=0)
#train_data=np.concatenate((data[0:45, :],data[50:95, :],data[100:145, :]),axis = 0)
train_data
#train_target=np.concatenate((target[0:45],target[50:95],target[100:145]),axis = 0)
train_target
#test_data=np.concatenate((data[45:50, :],data[95:100, :],data[145:150, :]),axis = 0)
test_data
#test_target=np.concatenate((target[45:50],target[95:100],target[145:150]),axis = 0)
test_target
clf=DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=6)
clf.fit(train_data, train_target)
traindata=clf.predict(train_data)
testdata=clf.predict(test_data)
sum=0
for i in range(45):
    if testdata[i]==test_target[i]:
        sum=sum+1
sum
print('accuracy=',sum*100/45,'%')
#Decision tree








