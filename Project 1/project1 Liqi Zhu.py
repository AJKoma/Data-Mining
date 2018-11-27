# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 12:40:24 2017

@author: Liqi Zhu
"""

import numpy as np
import pandas as pd

Dataset=pd.read_csv('D:/Rochester/Data Mining/project1/adult.data',dtype=str,names=['age','workclass','fnlwgt','education','educationnum','maritalstatus','occupation','relationship','race','sex','capitalgain','capitalloss','hoursperweek','nativecountry','income'])
data=Dataset.as_matrix()
data=data.tolist()
print(np.array(data))

print(Dataset.info())
print(Dataset)

age=Dataset['age'].value_counts()
value=np.array(age.index)
support=np.array(age.values)
workclass=Dataset['workclass'].value_counts()
value2=np.append(value,np.array(workclass.index))
support2=np.append(support,np.array(workclass.values))
fnlwgt=Dataset['fnlwgt'].value_counts()
value3=np.append(value2,np.array(fnlwgt.index))
support3=np.append(support2,np.array(fnlwgt.values))
education=Dataset['education'].value_counts()
value4=np.append(value3,np.array(education.index))
support4=np.append(support3,np.array(education.values))
educationnum=Dataset['educationnum'].value_counts()
value5=np.append(value4,np.array(educationnum.index))
support5=np.append(support4,np.array(educationnum.values))
maritalstatus=Dataset['maritalstatus'].value_counts()
value6=np.append(value5,np.array(maritalstatus.index))
support6=np.append(support5,np.array(maritalstatus.values))
occupation=Dataset['occupation'].value_counts()
value7=np.append(value6,np.array(occupation.index))
support7=np.append(support6,np.array(occupation.values))
relationship=Dataset['relationship'].value_counts()
value8=np.append(value7,np.array(relationship.index))
support8=np.append(support7,np.array(relationship.values))
race=Dataset['race'].value_counts()
value9=np.append(value8,np.array(race.index))
support9=np.append(support8,np.array(race.values))
sex=Dataset['sex'].value_counts()
value10=np.append(value9,np.array(sex.index))
support10=np.append(support9,np.array(sex.values))
capitalgain=Dataset['capitalgain'].value_counts()
value11=np.append(value10,np.array(capitalgain.index))
support11=np.append(support10,np.array(capitalgain.values))
capitalloss=Dataset['capitalloss'].value_counts()
value12=np.append(value11,np.array(capitalloss.index))
support12=np.append(support11,np.array(capitalloss.values))
hoursperweek=Dataset['hoursperweek'].value_counts()
value13=np.append(value12,np.array(hoursperweek.index))
support13=np.append(support12,np.array(hoursperweek.values))
nativecountry=Dataset['nativecountry'].value_counts()
value14=np.append(value13,np.array(nativecountry.index))
support14=np.append(support13,np.array(nativecountry.values))
income=Dataset['income'].value_counts()
value15=np.append(value14,np.array(income.index))
support15=np.append(support14,np.array(income.values))
n=Dataset.shape[0]
m=Dataset.shape[1]

sup=support15/n
sup

C1raw=pd.Series(sup,value15)
C1raw

supd = []
for j in range(m):
        supd.append({})
        for i in range(n):
            c = Dataset.iat[i,j]
            supd[j][c] = supd[j].get(c,0)+1
supd

def lk(ck,minsup):
    lk=ck[ck>minsup]
    return lk

L1=C1raw[C1raw>0.5]
L1
#Ck to Lk

def create_C1(data_set):
    C1 = set()
    for t in data_set:
        for item in t:
            item_set = frozenset([item])
            C1.add(item_set)
    return C1

C1=create_C1(data)
C1

def Ck(Lk_1,k):
    Ck = set()
    len_Lk_1 = len(Lk_1)
    list_Lk_1 = list(Lk_1)
    for i in range(len_Lk_1):
        for j in range(1,len_Lk_1):
            l1 = list(list_Lk_1[i])
            l2 = list(list_Lk_1[j])
            l1.sort()
            l2.sort()
            if l1[0:k-2] == l2[0:k-2]:
                Ck_item = list_Lk_1[i] | list_Lk_1[j]
    return Ck

def generate_Lk_by_Ck(data_set, Ck, min_support, support_data):
    Lk = set()
    item_count = {}
    for t in data_set:
        for item in Ck:
            if item.issubset(t):
                if item not in item_count:
                    item_count[item] = 1
                else:
                    item_count[item] += 1
    t_num = float(len(data_set))
    for item in item_count:
        if (item_count[item] / t_num) >= min_support:
            Lk.add(item)
            support_data[item] = item_count[item] / t_num
    return Lk

generate_Lk_by_Ck(data, C1, 0.5,supd)

# All frequent candidate k-itemsets
C1raw
L1raw=C1raw[C1raw>0.5]
L1raw
L1=generate_Lk_by_Ck(data, C1, 0.5,supd)
C2=Ck(L1,2)
L2=generate_Lk_by_Ck(data, C2, 0.5,supd)
C3=Ck(L2,3)
L3=generate_Lk_by_Ck(data, C3, 0.5,supd)

C1
L1
C2
L2
C3
L3
             





########FP Growth###########
from collections import defaultdict, namedtuple
Dataset=pd.read_csv('D:/Rochester/Data Mining/project1/adult.data',dtype=str,names=['age','workclass','fnlwgt','education','educationnum','maritalstatus','occupation','relationship','race','sex','capitalgain','capitalloss','hoursperweek','nativecountry','income'])
data=Dataset.as_matrix()

class treeNode:
    def __init__(self, nameValue, numOccur, parentNode):
        self.name = nameValue
        self.count = numOccur
        self.nodeLink = None 
        self.parent = parentNode 
        self.children = {} 

    def inc(self, numOccur):
        self.count += numOccur

    def disp(self, ind=1):
        print ('  ' * ind, self.name, ' ', self.count)
        for child in self.children.values():
            child.disp(ind + 1)

def createTree(dataSet, minSup=1):
    headerTable = {}
    for trans in dataSet:  
        for item in trans:
            headerTable[item] = headerTable.get(item, 0) + dataSet[trans]
    for k in list(headerTable):
        if headerTable[k] < minSup:
            del (headerTable[k])
    freqItemSet = set(headerTable.keys())
    if len(freqItemSet) == 0:
        return None, None
    for k in headerTable:
        headerTable[k] = [headerTable[k], None]
    retTree = treeNode('Null Set', 1, None)
    for tranSet, count in dataSet.items():
        localD = {}
        for item in tranSet:
            if item in freqItemSet:
                localD[item] = headerTable[item][0]
        if len(localD) > 0:
            orderedItems = [v[0] for v in sorted(localD.items(), key=lambda p: p[1], reverse=True)]
            updateTree(orderedItems, retTree, headerTable, count)
    return retTree, headerTable


def updateTree(items, inTree, headerTable, count):
    if items[0] in inTree.children:
        inTree.children[items[0]].inc(count)
    else:
        inTree.children[items[0]] = treeNode(items[0], count, inTree)
        if headerTable[items[0]][1] == None:
            headerTable[items[0]][1] = inTree.children[items[0]]
        else:
            updateHeader(headerTable[items[0]][1], inTree.children[items[0]])
    if len(items) > 1:
        updateTree(items[1::], inTree.children[items[0]], headerTable, count)

def updateHeader(nodeToTest, targetNode):
    while (nodeToTest.nodeLink != None):
        nodeToTest = nodeToTest.nodeLink
    nodeToTest.nodeLink = targetNode

simDat = data
simDat
def createInitSet(dataSet):
    retDict = {}
    for trans in dataSet:
        retDict[frozenset(trans)] = 1
    return retDict

initSet = createInitSet(data)
initSet
myFPtree, myHeaderTab = createTree(initSet, 3)
myFPtree.disp()

def ascendTree(leafNode, prefixPath):  
    if leafNode.parent != None:
        prefixPath.append(leafNode.name)
        ascendTree(leafNode.parent, prefixPath)


def findPrefixPath(basePat, treeNode):
    condPats = {}
    while treeNode != None:
        prefixPath = []
        ascendTree(treeNode, prefixPath)
        if len(prefixPath) > 1:
            condPats[frozenset(prefixPath[1:])] = treeNode.count
        treeNode = treeNode.nodeLink
    return condPats

def mineTree(inTree, headerTable, minSup, preFix, freqItemList):
    bigL = [v[0] for v in sorted(headerTable.items(), key=lambda p: str(p[1]))]
    for basePat in bigL:
        newFreqSet = preFix.copy()
        newFreqSet.add(basePat)
        freqItemList.append(newFreqSet)
        condPattBases = findPrefixPath(basePat, headerTable[basePat][1])
        myCondTree, myHead = createTree(condPattBases, minSup)
        if myHead != None:
            print ('conditional tree for: ',newFreqSet)
            myCondTree.disp(1)
            mineTree(myCondTree, myHead, minSup, newFreqSet, freqItemList)

