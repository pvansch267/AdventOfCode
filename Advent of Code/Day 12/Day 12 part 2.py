# 1. Open the file
with open("C:\\Users\\Paul\\Documents\\Advent of Code\\Day 12\\data.txt",'r') as raw_cypher_data:
    content = [line.strip() for line in raw_cypher_data.readlines()]

# 2. Set Key variables
dicCoordToDir = {0:'N',90:'E',180:'S',270:'W'}
dicDirToCoord = {'N':0,'E':90,'S':180,'W':270}
lstDirections = ['N','E','S','W']
dicDirectionTraveled = {'N':0,'E':0,'S':0,'W':0}
dicWayPoint = {'E':10,'N':1}
valManhattanDistance = 0

# 3. Define Key functions
def fnGetInstrDetail(instr):
    vDirectionDetail = instr[0]

    return vDirectionDetail

def fnGetInstrValue(instr):
    vDirectionValue = instr[1:]

    return vDirectionValue

# 1.1 Move Forward 
def fnMoveForward(dicWayPoint,dicDirectionTraveled,valInstruction):
    for direction in dicWayPoint:
        valDistanceTraveled = dicWayPoint[direction] * valInstruction
        dicDirectionTraveled[direction] = dicDirectionTraveled[direction] + valDistanceTraveled

    print(dicDirectionTraveled)
    return dicDirectionTraveled

# 1.2 Move Waypoint
def fnMoveWayPoint(dicWayPoint,strInstruction,valInstruction):
    
    dicUpdatedWayPoint = {}

    if strInstruction in dicWayPoint:
        dicWayPoint[strInstruction] = dicWayPoint[strInstruction] + valInstruction
    else:
        if strInstruction == 'N':
            dicWayPoint['S'] = dicWayPoint['S'] - valInstruction
        elif strInstruction == 'S':
            dicWayPoint['N'] = dicWayPoint['N'] - valInstruction
        elif strInstruction == 'E':
            dicWayPoint['W'] = dicWayPoint['W'] - valInstruction
        elif strInstruction == 'W':
            dicWayPoint['E'] = dicWayPoint['E'] - valInstruction

    for direction,value in dicWayPoint.items():
        if value < 0:
            valIncrement = 2
            valDirectionListIndex = lstDirections.index(direction)
            valIncrementShift = valDirectionListIndex + valIncrement
            value = value * -1

            if valIncrementShift > len(lstDirections):
                valIncrementShift = valIncrementShift - 4
            
            strUpdatedWayPoint = lstDirections[valIncrementShift]
            dicUpdatedWayPoint[strUpdatedWayPoint] = value
        else:
            dicUpdatedWayPoint[direction] = value

    print(dicUpdatedWayPoint)

    return dicUpdatedWayPoint


# 2   Change Direction
def fnTurnShip(dicWayPoint,lstDirections,strInstruction,valInstruction):
    dicUpdatedWayPoint = {}

    valIncrement = int(valInstruction / 90)
    
    if strInstruction == 'L':
        valIncrement = valInstruction * -1

    for direction in dicWayPoint:
        valDirectionListIndex = lstDirections.index(direction)

        valShiftbyIncrement = valDirectionListIndex + valIncrement

        if valShiftbyIncrement > len(lstDirections):
            valShiftbyIncrement = valShiftbyIncrement - len(lstDirections)
    
        strUpdatedWayPoint = lstDirections[valShiftbyIncrement]
        dicUpdatedWayPoint[strUpdatedWayPoint] = dicWayPoint[direction]
    
    return dicUpdatedWayPoint

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
    
    print('Instruction:',instr)
    print('Waypoint:',dicWayPoint)

    if strInstruction == 'F':
        dicDirectionTraveled = fnMoveForward(dicWayPoint,dicDirectionTraveled,valInstruction)
    elif strInstruction == 'L' or strInstruction == 'R':
        dicWayPoint = fnTurnShip(dicWayPoint,lstDirections,strInstruction,valInstruction)
    else:
        dicWayPoint = fnMoveWayPoint(dicWayPoint,strInstruction,valInstruction)

valManhattanDistance = fnGroupDistance(dicDirectionTraveled)

valManhattanDistance = sum(dicDirectionTraveled.values())

print(dicDirToCoord)
print(valManhattanDistance)
