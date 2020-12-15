
# Open document
password_data = open("C:\\Users\Paul\Documents\Advent of Code\Day 2\data.txt","r")

# Read through document and split into individual user passwords with defined criteria
content = password_data.readlines()
aryPasswordData = [x.split(' ') for x in content]

# Set inital valid password count
vValidPasswordCount = 0

def fnValidatePassword(vFirstIndex,vSecondIndex,vCriteria,vPassword):
    #***********************************************************************#
    # Test whether password has the correct number of Index matches         #
    #***********************************************************************#

    vIndexVerification = 0

    vIndexVerification = vIndexVerification + fnValidateIndex(vFirstIndex,vCriteria,vPassword)
    vIndexVerification = vIndexVerification + fnValidateIndex(vSecondIndex,vCriteria,vPassword)

    if vIndexVerification ==1:
        return 1
    else:
        return 0

def fnValidateIndex(vIndex,vCriteria,vPassword):
    #***********************************************************************#
    # Test index in password matches the predefined criteria                #
    #***********************************************************************#

    if vPassword[vIndex] == vCriteria:
        return 1
    else:
        return 0

# Loop through password data array and test individual passwords against their defined criteria
for pwd in aryPasswordData:
    vFirstPosition = int(pwd[0].split('-')[0])
    vSecondPosition = int(pwd[0].split('-')[1])

    vFirstIndex = vFirstPosition - 1
    vSecondIndex = vSecondPosition - 1

    vCriteria = pwd[1].strip((':'))
    vPassword = pwd[2].strip()
    
    vValidPasswordCount = vValidPasswordCount + fnValidatePassword(vFirstIndex,vSecondIndex,vCriteria,vPassword)

print(vValidPasswordCount)
