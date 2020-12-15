# 1. Open the file
with open("C:\\Users\\Paul\\Documents\\Advent of Code\\Day 12\\data.txt",'r') as raw_cypher_data:
    content = [line.strip() for line in raw_cypher_data.readlines()]

# 2. Set Key variables
dicCoordToDir = {0:'N',90:'E',180:'S',270:'W'}
dicDirToCoord = {'N':0,'E':90,'S':180,'W':270}
dicDirectionTraveled = {'N':0,'E':0,'S':0,'W':0}
strShipDirection = 'E'
valManhattanDistance = 0

# 3. Define Key functions
def fnGetInstrDetail(instr):
    vDirectionDetail = instr[0]

    return vDirectionDetail

def fnGetInstrValue(instr):
    vDirectionValue = instr[1:]

    return vDirectionValue

# 1.1 Move Forward 
def fnMoveForward(valShipDirection,dicDirectionTraveled,valInstruction):
    dicDirectionTraveled[valShipDirection] = dicDirectionTraveled[valShipDirection] + valInstruction
    print(dicDirectionTraveled)
    return dicDirectionTraveled

# 1.2 Move Direction
def fnMoveDirection(strInstruction,dicDirectionTraveled,valInstruction):
    dicDirectionTraveled[strInstruction] = dicDirectionTraveled[strInstruction] + valInstruction
    print(dicDirectionTraveled)
    return  dicDirectionTraveled

# 2   Change Direction
def fnTurnShip(strShipDirection,strInstruction,valInstruction,dicDirToCoord,dicCoordToDir):
    valCoord = dicDirToCoord[strShipDirection]
    
    if strInstruction == 'L':
        valInstruction = valInstruction * -1
    
    valUpdatedCoord = valCoord + valInstruction

    if valUpdatedCoord >= 360:
        valUpdatedCoord = valUpdatedCoord - 360
    elif valUpdatedCoord < 0:
        valUpdatedCoord = valUpdatedCoord + 360
    
    strShipDirection = dicCoordToDir[valUpdatedCoord]
    
    return strShipDirection

# 3   Find True Movement
def fnGroupDistance(dicDirectionTraveled):
    valGroupedDirectionNorth = dicDirectionTraveled['N'] - dicDirectionTraveled['S']
    valGroupedDirectionEast = dicDirectionTraveled['E'] - dicDirectionTraveled['W']

    if valGroupedDirectionNorth > 0:
        dicDirectionTraveled['N'] = valGroupedDirectionNorth 
        dicDirectionTraveled['S'] = 0
    else:
        dicDirectionTraveled['S'] = valGroupedDirectionNorth * -1
        dicDirectionTraveled['N'] = 0

    if valGroupedDirectionEast > 0:
        dicDirectionTraveled['E'] = valGroupedDirectionEast 
        dicDirectionTraveled['W'] = 0
    else:
        dicDirectionTraveled['W'] = valGroupedDirectionEast * -1 
        dicDirectionTraveled['E'] = 0

    return dicDirectionTraveled

# 4. Run Application
for instr in content:
    valInstruction = int(fnGetInstrValue(instr))
    strInstruction = fnGetInstrDetail(instr)

    if strInstruction == 'F':
        dicDirectionTraveled = fnMoveForward(strShipDirection,dicDirectionTraveled,valInstruction)
    elif strInstruction == 'L' or strInstruction == 'R':
        strShipDirection = fnTurnShip(strShipDirection,strInstruction,valInstruction,dicDirToCoord,dicCoordToDir)
    else:
        dicDirectionTraveled = fnMoveDirection(strInstruction,dicDirectionTraveled,valInstruction)

valManhattanDistance = fnGroupDistance(dicDirectionTraveled)

valManhattanDistance = sum(dicDirectionTraveled.values())

print(dicDirToCoord)
print(valManhattanDistance)

'''


def fnUpdateOppDirection(instrDetail,instrVal,dicDirectionTraveled):
    
    if vShipDirection == 'North':
        if dicDirectionTraveled['South'] > 0:
            vRemainder = dicDirectionTraveled['South'] - instrVal
    elif vShipDirection == 'South':
        if dicDirectionTraveled['North'] > 0:
            vRemainder = dicDirectionTraveled['North'] - instrVal
    elif vShipDirection == 'East':
        if dicDirectionTraveled['West'] > 0:
            vRemainder = dicDirectionTraveled['West'] - instrVal
    elif vShipDirection == 'West':
        if dicDirectionTraveled['East'] > 0:
            vRemainder = dicDirectionTraveled['East'] - instrVal

    return vRemainder






def fnGetCoord(vShipDirection, dicDirToCoord):
    return dicDirToCoord[vShipDirection]

def fnUpdateCoord(coord,instrVal,instrDetail):
    if instrDetail == 'L':
        instrVal = instrVal * -1
    
    VUpdatedCoord = coord + instrVal

    if VUpdatedCoord >= 360:
        VUpdatedCoord = VUpdatedCoord - 360
    
    return VUpdatedCoord

print(fnGetCoord(vShipDirection, dicDirToCoord))

'''