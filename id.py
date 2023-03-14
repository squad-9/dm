import pandas as pd
import math

df = pd.read_csv('playCricket.csv')
decisionCol = 'answer'

def getCount(df,column,classLabel):
    return len(df[df[column] == classLabel])


def IEDecision(df):
    entropy = 0
    for label in df[decisionCol].unique():
        labelCount = getCount(df,decisionCol,label)
        entropy-=(labelCount/len(df))*(math.log2(labelCount/len(df)))
    return entropy

def IG(df,column):
    gain = IEDecision(df)
    for label in df[column].unique():
        labelCount = getCount(df,column,label)
        newdf = df[df[column]==label]
        sublabelEntropy = 0
        for decisonVar in df[decisionCol].unique():
            sublabelCount = getCount(newdf,decisionCol,decisonVar)
            if sublabelCount != 0:
                sublabelEntropy-=(sublabelCount/len(newdf))*(math.log2(sublabelCount/len(newdf)))
        gain-=(labelCount/len(df))*sublabelEntropy
    return gain

def constructTree(df,path):
    maxIg = 0
    maxCol = None
    for col in df.columns:
        if col == decisionCol:
            continue
        if maxIg<IG(df,col):
            maxIg = IG(df,col)
            maxCol = col
    if maxIg==0:
        path.append(df.iloc[-1][decisionCol])
        print(" --> ".join(path))
        return
    for label in df[maxCol].unique():
        constructTree(df[df[maxCol]==label],path+[str(maxCol) + "(" +str(label) + ")"])

constructTree(df,[])