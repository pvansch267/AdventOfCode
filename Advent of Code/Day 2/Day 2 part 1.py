
password_data = open("C:\\Users\Paul\Documents\Advent of Code\Day 2\data.txt","r")

content = password_data.readlines()

aryPasswordData = [x.split(' ') for x in content]

vValidPasswordCount = 0

def fnValidatePassword(vMinLength,vMaxLength,vCriteria,vPassword):
    
    vOccurence = fnCriteriaCount(vCriteria,vPassword)

    if vOccurence < vMinLength or vOccurence > vMaxLength:
        return 0
    else:
        return 1

def fnCriteriaCount(vCriteria,vPassword):
    vOccurence = 0
    for letter in vPassword:
        if letter == vCriteria:
            vOccurence += 1
    
    return vOccurence


for pwd in aryPasswordData:
    vMinLength = int(pwd[0].split('-')[0])
    vMaxLength = int(pwd[0].split('-')[1])
    vCriteria = pwd[1].strip((':'))
    vPassword = pwd[2].strip()
    
    vValidPasswordCount = vValidPasswordCount + fnValidatePassword(vMinLength,vMaxLength,vCriteria,vPassword)

print(vValidPasswordCount)
