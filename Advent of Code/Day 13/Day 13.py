# Open the file
with open("C:\\Users\\Paul\\Documents\\Advent of Code\\Day 13\\data.txt",'r') as raw_cypher_data:
    content = [line.strip() for line in raw_cypher_data.readlines()]

tmStmpEarliest = int(content[0])
lstBusList = content[1].split(',')

def fnGetBusDepartureTime(bus,tmStmpEarliest):
    if bus == 'x':
        return 'Out of Service'
    else:
        tmDepartureTime = 0
        bus = int(bus)
        while tmDepartureTime <= tmStmpEarliest:
            tmDepartureTime += bus
        
        return tmDepartureTime

def fnGetPossibleDepartureDic(lstBusList,tmStmpEarliest):
    dicPossibleDeapartures = {}

    for bus in lstBusList:
        if bus != 'x':
            dicPossibleDeapartures[bus] = fnGetBusDepartureTime(bus,tmStmpEarliest)
    
    return dicPossibleDeapartures

def fnGetEarliestAvailableBus(dicDepartureTime,tmStmpEarliest):
    tmpEarliestBus = []

    for key, value in dicDepartureTime.items():
        vWaitTime = value - tmStmpEarliest

        if len(tmpEarliestBus) == 0 or vWaitTime < tmpEarliestBus[2]:
            tmpEarliestBus = []
            tmpEarliestBus.append(key)
            tmpEarliestBus.append(value)
            tmpEarliestBus.append(vWaitTime)
    
    return tmpEarliestBus

dicDepartureTime = fnGetPossibleDepartureDic(lstBusList,tmStmpEarliest)

lstEarliestBus = fnGetEarliestAvailableBus(dicDepartureTime,tmStmpEarliest)

vProdIDWaitTime = int(lstEarliestBus[0]) * int(lstEarliestBus[2])

print(vProdIDWaitTime)