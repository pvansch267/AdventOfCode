# Open the file
with open("C:\\Users\\Paul\\Documents\\Advent of Code\\Day 9\\data.txt",'r') as raw_cypher_data:
    content = [int(line.strip()) for line in raw_cypher_data.readlines()]

# Set Key variables
vPreambleLength = 25
vPreambleList = []
vXMASList = []
vFullList = []
flIdentifiedInvalid = False

# Populate all lists
for idx, val in enumerate(content):
    if idx < vPreambleLength:
        vPreambleList.append(val)
    else:
        vXMASList.append(val)
    vFullList.append(val)

# Check list val
def fnValidCypherSumValue(sumval,list):
    for idx, vFirstVal in enumerate(list):
        vSecondVal = sumval - vFirstVal

        if vSecondVal in list:
            if list.index(vSecondVal) != idx:
                return True
    
    return False

# Update preamble list
def fUpdatePreambleList(val,list):
    list.pop(0)
    list.append(val)
    return list

# Update XMAS list
def fnUpdateXMASList(val,list):
    list.remove(val)
    return list

# Fetch new from list
def fnGetNewVal(list):
    vSumVal = list.pop(0)

    return vSumVal

# Part 1 Primary Function
def fnIdentifyInvalidEntry():
    global flIdentifiedInvalid
    
    # Get new value to test from XMAS List
    vSumVal = fnGetNewVal(vXMASList)

    # Test value against preamble list
    flValidCypher = fnValidCypherSumValue(vSumVal,vPreambleList)

    while not flIdentifiedInvalid:
        if flValidCypher:
            # If value is valid part of cypher, update preamble list and recursively call function
            fUpdatePreambleList(vSumVal,vPreambleList)
            vSumVal = fnIdentifyInvalidEntry()
        else:
            # If value is invalid part of cypher, set invalid flag and return value
            flIdentifiedInvalid = True

            return vSumVal

    # Return invalid value
    return vSumVal

# Part 2 - Search function
def fnMainFunctionPart2(vInvalidEntry,list):
    
    # Set key variables
    vLenXMASCypher = len(list)
    vCurrentSum = 0 
    lstContiguousSum = []
    idx = 0

    while idx <= vLenXMASCypher:

        if vCurrentSum == vInvalidEntry:
            # If running total is equal to invalid to invalid entry break out of loop
            break
        elif vCurrentSum > vInvalidEntry:
            while vCurrentSum > vInvalidEntry:
                # While running total is larger than invalid entry, remove starting point of list
                vCurrentSum -= lstContiguousSum[0]
                lstContiguousSum.pop(0)

            if vCurrentSum == vInvalidEntry:
                # If running total is equal to invalid to invalid entry break out of loop
                break
            
        if idx < vLenXMASCypher:
            # Add next value in list to running total and append to Contiguous Sum list
            vCurrentSum += list[idx]
            lstContiguousSum.append(list[idx])

        # Increment index
        idx += 1
    
    return lstContiguousSum

vInvalidEntry = fnIdentifyInvalidEntry()

print('Part 1 Solution:', vInvalidEntry)

vContiguousSumList = fnMainFunctionPart2(vInvalidEntry,vFullList)

print('Sum of List:', sum(vContiguousSumList))

vContiguousMin = min(vContiguousSumList)
vContiguousMax = max(vContiguousSumList)

print('Min of List:', vContiguousMin)
print('Max of List:', vContiguousMin)

print('Part 2 Solution:', vContiguousMax + vContiguousMin)