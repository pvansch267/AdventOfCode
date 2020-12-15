import pandas as pd

df = pd.read_csv("C:\\Users\\Paul\\Documents\\Advent of Code\\Day 11\\test_data.txt",sep=" ",header = None)
bdColumnLength = len(df.iloc[0,0])
df = df.iloc[:,0].str.split('', bdColumnLength, expand=True)
df = df.drop(df.columns[0],axis=1)
df = df.T.reset_index(drop=True).T
bdRowLength = df.shape[1] -1
dicSeatType = {'L':'Empty',
               '#':'Occupied',
               '.':'Gap'}

dicAdjSeatsLocation = {'L':(-1,0),'UL':(-1,-1),
                       'U':(0,-1),'UR':(1,-1),
                       'R':(1,0),'DR':(1,1),
                       'D':(0,1),'DL':(-1,1)
                      }

def fnGetAdjSeatLocation(cdRow,cdColumn):
    dicAdjSeats = {}
    lstAdjSeats = []
    for adjSeat in dicAdjSeatsLocation:
        row = cdRow + dicAdjSeatsLocation[adjSeat][0]
        column = cdColumn + dicAdjSeatsLocation[adjSeat][1]
        lstAdjSeats.append([row,column])
        dicAdjSeats[adjSeat] = [row,column]

    return lstAdjSeats

def fnGetValidAdjSeatLocation(cdRow,cdColumn):
    lstAdjSeats = []
    for adjSeat in dicAdjSeatsLocation:
        row = cdRow + dicAdjSeatsLocation[adjSeat][1]
        column = cdColumn + dicAdjSeatsLocation[adjSeat][0]
        blSeatID = fnValidAdjSeatID([row,column],9,9)

        if not blSeatID:
            continue

        vAdjSeatStatus = df.iloc[row,column]
        while vAdjSeatStatus != 'L' and vAdjSeatStatus != '#':
            row = row + dicAdjSeatsLocation[adjSeat][1]
            column = column + dicAdjSeatsLocation[adjSeat][0]
            blSeatID = fnValidAdjSeatID([row,column],9,9)
            if not blSeatID:
                break

            vAdjSeatStatus = df.iloc[row,column]
        
        if blSeatID:
            lstAdjSeats.append([row,column])

    return lstAdjSeats

def fnValidAdjSeatID(seat,bdRow,bdColumn):
    if seat[0] >= 0 and seat[0] < bdRow:
        if seat[1] >= 0 and seat[1] <= bdColumn:
            return True

    return False

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
    if seatValue == "#" and lstValidAdjSeats.count('#') >=5:
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
            #lstAdjSeats = fnGetAdjSeatLocation(index,columnName)
            lstAdjSeats = fnGetValidAdjSeatLocation(index,columnName)
          #  lstValidSeats = fnValidatedAdjSeatLocation(lstAdjSeats,9,9)
            # 2.2 What is the value of the adjoining seats
            lstAdjSeatStatus = fnGetAllAdjSeatStatus(lstAdjSeats)
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

    print(df)

print(dicCountSeatStatus)