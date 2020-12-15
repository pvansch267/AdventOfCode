from functools import reduce

# Open document
map_data = open("C:\\Users\\Paul\\Documents\\Advent of Code\Day 3\\data.txt","r")

# Read through document and split into individual user passwords with defined criteria
content = map_data.readlines()
aryMapData = [x.strip() for x in content]

vTobogganPath = [1,3]
vTobogganProgress = [1,1]
vYCoordinate = 1
vTobogganPossibleRoutes = [[1,1],[1,3],[1,5],[1,7],[2,1]]
vTreesEncountered = []

def fnIdentifyTreeinPath(map_horizontal,vXDistance):
    # ************************************************************ #
    # Traverse across the map for the defined vXRoute value and    #
    # check whether there is a tree at that coordinate             #
    # ************************************************************ #

    coordReached = False   
    count = 1
    
    while not coordReached:
        for steps in map_horizontal:
            if count == vXDistance:
                coordReached = True
                if steps == "#":
                    flTreeIdentified = 1
                else:
                    flTreeIdentified = 0
                break
            count +=1

    return flTreeIdentified

def fnNavigateMap(vMap,vProgress,vRoute):

    vCountTrees = 0
    vYDistance = 1
    vMapLine = 1

    for line in vMap:
        map_horizontal = line
        vXDistance = vProgress[1]

        if vMapLine == vProgress[0]:
            vCountTrees = vCountTrees + fnIdentifyTreeinPath(map_horizontal,vXDistance)
            vProgress = [x + y for x, y in zip(vRoute, vProgress)]

        vYDistance += 1
        vMapLine += 1

    return vCountTrees

for path in vTobogganPossibleRoutes:
    vTreesEncountered.append(fnNavigateMap(aryMapData,vTobogganProgress,path))

vProductOfTreesInRoutes = reduce((lambda x,y: x*y),vTreesEncountered)

print('Total trees encountered:', vProductOfTreesInRoutes)
