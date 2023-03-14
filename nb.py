
import pandas as pd

df = pd.read_csv(r'playCricket.csv')
decisionCol = "answer"

def calcCondProb(col,colVal,decisionVal):
    return (len(df[(df[col]==colVal) & (df[decisionCol]==decisionVal)])/len(df[df[decisionCol]==decisionVal]))

qn = {
    "outlook" : "sunny",
    "temperature" : "cool",
    "humidity" : "high",
    "wind" : "strong"
}

def fn():
    ans = None
    ans_val = -1
    for decisionVal in df[decisionCol].unique():
        val = len(df[df[decisionCol]==decisionVal])/len(df)
        for col,colVal in qn.items():
            val*=calcCondProb(col,colVal,decisionVal)
        print(val)
        if val>=ans_val:
            ans = decisionVal
            ans_val = val
    return ans

print(fn())