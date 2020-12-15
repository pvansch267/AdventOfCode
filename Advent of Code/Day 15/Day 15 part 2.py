with open("C:\\Users\\Paul\\Documents\\Advent of Code\\Day 15\\test_data.txt",'r') as raw_cypher_data:
    lstStartingNumbers = [int(i) for i in raw_cypher_data.read().split(',')]

print('Starting Numbers:', lstStartingNumbers)

# 1. Define Key Variables
varTurnCount = 0
dicTurns = {}
varLastTurn = 0

# 2. Begin by reading start numbers
for stnum in lstStartingNumbers:
    varTurnCount += 1
    varLastTurn = stnum 
    dicTurns[varTurnCount] = varLastTurn

#print(dicTurns)
#print(len([key for key,value in dicTurns.items() if value == 6][-2:]))

# 3.
while varTurnCount < 30000000:
    varTurnCount += 1

#    print('Turn count:',varTurnCount)
#    print('History of turns:',dicTurns)
#    print('Last turn:',varLastTurn)

    ixAppearances = [key for key,value in dicTurns.items() if value == varLastTurn][-2:]

    if len(ixAppearances) < 2:
        varLastTurn = 0
    else:
        varLastTurn = ixAppearances[-1]-ixAppearances[-2]
    
    dicTurns[varTurnCount] = varLastTurn
    
print(varLastTurn)

'''
# 2. Begin by reading start numbers
for stnum in lstStartingNumbers:
    varTurnCount += 1
    dicTurns[varTurnCount] = varLastTurn
    varLastTurn = stnum

print('Turn count:',varTurnCount)
print('History of turns:',dicTurns)
print('Last turn:',varLastTurn)

# 3. Begin memory component of game
while varTurnCount < 30000000:
    varTurnCount += 1

#    print('Turn count:',varTurnCount)
#    print('History of turns:',lstTurns)
#    print('Last turn:',varLastTurn)

    varCountLastTurn = lstTurns.count(varLastTurn)

    if varCountLastTurn > 1:
        lstTurns.reverse()
        valIndexLastAppearance = len(lstTurns) - lstTurns.index(varLastTurn)
#        print('Last appearance:', valIndexLastAppearance)
        valIndexSecondLastAppearance = len(lstTurns) - lstTurns.index(varLastTurn,lstTurns.index(varLastTurn) + 1)
#        print('Second last appearance:', valIndexSecondLastAppearance)
        varTurn = valIndexLastAppearance - valIndexSecondLastAppearance
#        print('Difference:', varTurn)
        lstTurns.reverse()
        lstTurns.append(varTurn)
        varLastTurn = varTurn
    else:
        lstTurns.append(0)
        varLastTurn = 0

print('Last Turn:', varLastTurn)

'''