import pandas as pd
df = pd.read_csv(r'D:\\edu\\sem 8\\DM\\LAB\\aprioriDS.csv', header=None)


def getCount(itemset):
    count = 0
    for ele in tx_arr:
        if set(itemset).issubset(set(ele)):
            count += 1
    return count


def crossProduct(itemset):
    arr = []
    k = len(itemset[0])-1
    for i in range(len(itemset)):
        for j in range(i+1, len(itemset)):
            if(itemset[i][:k] == itemset[j][:k]):
                arr.append(itemset[i] + [itemset[j][-1]])
    return arr


def genSubset(arr):
    ans = []

    def helper(ind, curr):
        if(len(arr)-1 == len(curr)):
            ans.append(curr)
            return
        for i in range(ind, len(arr)):
            helper(i+1, curr+[arr[i]])
    helper(0, [])
    return ans


def isSubset(arr1, arr2):
    for ele in arr2:
        if arr1 == ele:
            return True
    return False


def genAllSubset(arr):
    ans = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            ans.append([arr[i:j], arr[:i]+arr[j:]])
    return ans


minSup = 2

L = set()
tx_arr = []

for i in range(df.shape[0]):
    d_arr = []
    for j in range(df.shape[1]):
        if(type(df.iloc[i][j]) is str):
            L.add(df.iloc[i][j])
            d_arr.append(df.iloc[i][j])
    tx_arr.append(d_arr)

L = list(L)
L.sort()

L = [[ele] for ele in L]

C = []

for ele in L:
    if(getCount(ele) >= minSup):
        C.append(ele)

freq_itemset = []

while(True):
    if(len(C) > 0):
        freq_itemset.append(C)
        L = crossProduct(C)
        print(len(freq_itemset[-1][0]), " - ", freq_itemset[-1])
    if(len(L) == 0 or len(C) == 0):
        break
    C = []
    if(len(L[0]) <= 2):
        for ele in L:
            if(getCount(ele) >= minSup):
                C.append(ele)
    else:
        for ele in L:
            subset = genSubset(ele)
            flag = True
            for ele1 in subset:
                if not isSubset(ele1, freq_itemset[-1]):
                    flag = False
                    break
            if(flag):
                if(getCount(ele) >= minSup):
                    C.append(ele)

# Association Rule
confidence = 0.7
for i in range(1, len(freq_itemset)):
    ele = freq_itemset[i]
    for ele1 in ele:
        allSubset = genAllSubset(ele1)
        for ele2 in allSubset:
            l, s_l = ele2[0], ele2[1]
            if(getCount(l+s_l)/getCount(l) >= confidence):
                print(l, "-->", s_l)
            if(getCount(l+s_l)/getCount(s_l) >= confidence):
                print(s_l, "-->", l)
        print()
