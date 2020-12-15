import pandas as pd

df = pd.read_csv("C:\\Users\\Paul\\Documents\\Advent of Code\\Day 11\\data.txt",sep=" ",header = None)
bdColumnLength = len(df.iloc[0,0])
df = df.iloc[:,0].str.split('', bdColumnLength, expand=True)
df = df.drop(df.columns[0],axis=1)
df = df.T.reset_index(drop=True).T
print(df)
bdRowLength = df.shape[1] -1
print(df)
dicSeatType = {'L':'Empty',
               '#':'Occupied',
               '.':'Gap'}

dicAdjSeatsLocation = {0:(-1,0),1:(-1,1),
                       2:(0,1),3:(1,1),
                       4:(1,0),5:(1,-1),
                       6:(0,-1),7:(-1,-1)
                      }

def fnGetAdjSeatLocation(cdRow,cdColumn):
    lstAdjSeats = []
    for adjSeat in dicAdjSeatsLocation:
        row = cdRow + dicAdjSeatsLocation[adjSeat][0]
        column = cdColumn + dicAdjSeatsLocation[adjSeat][1]
        lstAdjSeats.append([row,column])

    return lstAdjSeats

def fnValidatedAdjSeatLocation(lst,bdRow,bdColumn):
    lstValidSeats = []
    for seat in lst:
        if seat[0] >= 0 and seat[0] < bdRow:
            if seat[1] >= 0 and seat[1] <= bdColumn:
                lstValidSeats.append(seat)

    return lstValidSeats

def fnGetSeatStatus(cdRow,cdColumn):
    return df.iloc[cdRow,cdColumn]

def fnGetAllAdjSeatStatus(lstAdjSeats):
    lstAdjSeatStatus = []
    for seat in lstAdjSeats:
        lstAdjSeatStatus.append(fnGetSeatStatus(seat[0],seat[1]))
    return lstAdjSeatStatus

def fnFillEmptySeat(x):
    return x.replace('L','#')

def fnEmptyFilledSeat(x):
    return x.replace('#','L')

def fnGetSeatChangeValidity(lstValidAdjSeats,seatValue):
    if seatValue == "#" and lstValidAdjSeats.count('#') >=4:
        return True
    elif seatValue == "L" and "#" not in lstValidAdjSeats:
        return True
    else:
        return False

# 1. Fill All Empty Seats
df = df.applymap(fnFillEmptySeat)
count = df.shape[0] * df.shape[1]

print(df)
# 2. Iterate Over each seat,

lstSeatChanges = []

while count > 0:
    dicCountSeatStatus = {'#':0,'L':0,'.':0}
    print('Changes:', count)
    count = 0
    #for columnName in range(10):
    for index, row in df.iterrows():
        lstRowSeatChanges = []
        for columnName, columnData in df.iteritems():
            # 2.1 What is the value of the seat
            vSeatStatus = fnGetSeatStatus(index,columnName)
            dicCountSeatStatus[vSeatStatus] += 1
            vSeatID = [index,columnName]
            lstAdjSeats = fnGetAdjSeatLocation(index,columnName)
            lstValidSeats = fnValidatedAdjSeatLocation(lstAdjSeats,93,93)
            # 2.2 What is the value of the adjoining seats
            lstAdjSeatStatus = fnGetAllAdjSeatStatus(lstValidSeats)
            # 2.3 Is the seat valid for a seat change
            blRequiresChange = fnGetSeatChangeValidity(lstAdjSeatStatus,vSeatStatus)
        #  print(blRequiresChange)
            lstRowSeatChanges.append(blRequiresChange)
            if blRequiresChange:
                count += 1
        lstSeatChanges.append(lstRowSeatChanges)
#    print('\n\n\nStarting Point')

    for idxRow,lstCol in enumerate(lstSeatChanges):
        lstColumnSeatChange = lstCol
        for idxColumn,blChange in enumerate(lstColumnSeatChange):
            if blChange:
                # 2.4 change seat
                if df.iloc[idxRow,idxColumn] == "L":
                    df.iloc[idxRow,idxColumn] = "#"
                else:
                    df.iloc[idxRow,idxColumn] = "L"

    lstSeatChanges = []

#    print(df)

print(dicCountSeatStatus)