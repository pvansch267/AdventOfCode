import itertools 
from functools import reduce

# Open the file
with open("C:\\Users\\Paul\\Documents\\Advent of Code\\Day 10\\data.txt",'r') as raw_cypher_data:
    content = [int(line.strip()) for line in raw_cypher_data.readlines()]

content.sort()

vBuiltIn = lambda max : max + 3
vBaseSocket = 0
dicDifference = {1:0,3:0}
lstSockets = [vBaseSocket]

vBagTotal = sum(content)

def fnCheckNextVal(idx, dataList, vCurrentSocket):
    vDifference = dataList[idx] - vCurrentSocket
    if vDifference <= 3:
        return True
    return False

def fnCheckSecondaryVal(idx, dataList):
    vDifference = dataList[idx + 1] - dataList[idx]
    if vDifference <= 3:
        return True    
    return False

def fnUpdateSocketListandDic(val,vCurrentSocket):
    global lstSockets, dicDifference
    
    lstSockets.append(val)
    vDifference = val - vCurrentSocket
    dicDifference[vDifference] += 1

idx = 0

vCountBagChargers = len(content)

while vCountBagChargers > 0:
    # Get current socket
    vCurrentSocket = lstSockets[-1]

    vSocketVal = content[idx]

    if idx + 1 < vCountBagChargers:
        
        # Check the next value in the list
        flValidOption = fnCheckNextVal(idx, content, vCurrentSocket)

        if flValidOption:
            flValidFollowingOption = fnCheckSecondaryVal(idx, content)
            if flValidFollowingOption:
                fnUpdateSocketListandDic(vSocketVal,vCurrentSocket)

    else:
        fnUpdateSocketListandDic(vSocketVal,vCurrentSocket)

    content.pop(idx)
    vCountBagChargers = len(content)

vCurrentSocket = lstSockets[-1]

fnUpdateSocketListandDic(vBuiltIn(vCurrentSocket),vCurrentSocket)

result = dicDifference[1] * dicDifference[3]

vCombinationCoun = 1

lstCombinationSets = []
lstSet = []

vSocketListChargers = len(lstSockets)

while vSocketListChargers > 0:
    vSocket = lstSockets[idx]
    if vSocketListChargers > 1:
        if lstSockets[idx + 1] - lstSockets[idx] == 1:
            lstSet.append(lstSockets[idx])
            lstSockets.remove(vSocket)
        else:
            lstSet.append(lstSockets[idx])
            lstSockets.remove(vSocket)
            lstCombinationSets.append(lstSet)
            lstSet = []
    else:
        lstSet.append(lstSockets[idx])
        lstSockets.remove(vSocket)
        lstCombinationSets.append(lstSet)
        lstSet = []
    vSocketListChargers = len(lstSockets)
    idx = 0

def fnGetSubSets(s,n):
    return list(itertools.combinations(s,n))

lstPossibleCombinations = []

def fnValidStartCombination(list,val):
    if list[0] == val:
        return True
    else:
        return False

def fnValidEndCombination(list,val):
    if list[-1] == val:
        return True
    else:
        return False

def fnValidGapCombination(list):
    flValidGap = False    
    for id,val in enumerate(list):
        if id < len(list)-1:
            if list[id+1] - list[id] <= 3:
                flValidGap = True
            else:
                flValidGap = False
    return flValidGap

def fnValidCombinationSignoff(list,vMinX,vMaxX):
    flValidCombination = True

    flValidCombination = fnValidStartCombination(list,vMinX)
    if not flValidCombination:
        return False
    flValidCombination = fnValidEndCombination(list,vMaxX)
    if not flValidCombination:
        return False
    flValidCombination = fnValidGapCombination(list)
    if not flValidCombination:
        return False

    return flValidCombination

for x in lstCombinationSets:
    vLength = len(x)
    vMinX = x[0]
    vMaxX = x[-1]
    flValidCombination = False
    i = 2 
    count = 0

    if vLength <= 2:
        count += 1
    else:
        while i <= vLength:
            vPossibleCombination = fnGetSubSets(x,i)

            for set in vPossibleCombination:
                flValidCombination = fnValidCombinationSignoff(set,vMinX,vMaxX)

                if flValidCombination:
                    count += 1
                
            i += 1
    
    lstPossibleCombinations.append(count)

test = reduce((lambda  x, y: x * y), lstPossibleCombinations)
    
print(test)
