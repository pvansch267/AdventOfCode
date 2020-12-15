import re

passport_data = open("C:\\Users\\Paul\Documents\\Advent of Code\\Day 4\\data.txt","r")

# Load data into a raw_batch_file
raw_batch_file= []

content = passport_data.read()
content = content.split('\n\n')


raw_batch_file.append([x.replace('\n',' ') for x in content])
raw_batch_file = raw_batch_file[0]

passport_fields = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
passport_optional_fields = ['cid']
valid_passports = 0

def fnCreateDocumentDictionary(data):
    data = data.strip()
    doc_data_dict = {data_entry.split(':')[0]:data_entry.split(':')[1] for data_entry in data.split(' ')}
    return doc_data_dict

def fnValidateoptionalFields(missing,optional):
    critical_failures = [x for x in missing if x not in optional]
    if len(critical_failures)>0:
        return False
    else:
        return True

def fnValidatePassport(document,requirement,optional):
    vFieldsPresent = False
    vFieldStatus = []
    
    if all(category in document for category in requirement):
        vFieldsPresent = True
    else:
        vMissingElement = (set(requirement) - document.keys())
        print(vMissingElement)
        vFieldsPresent = fnValidateoptionalFields(vMissingElement,optional)
    
    if vFieldsPresent:
        vFieldStatus.append(fnValidYear(document.get('byr'),1920,2002))
        vFieldStatus.append(fnValidYear(document.get('iyr'),2010,2020))
        vFieldStatus.append(fnValidYear(document.get('eyr'),2020,2030))
        vFieldStatus.append(fnValidHeight(document.get('hgt')))
        vFieldStatus.append(fnValidHair(document.get('hcl')))
        vFieldStatus.append(fnValidEye(document.get('ecl')))
        vFieldStatus.append(fnValidPassportID(document.get('pid')))
        if False in vFieldStatus:
            return False
        else:
            return True
    else:
        return False
    
def fnValidYear(value,min,max):
    try:
        year = int(value)
        if year >= min and year <= max:
            return True
        else:
            return False
    except:
        return False

def fnValidHeight(value):
    try:
        height = int(value[:-2])
        hType = value[-2:]

        if hType == "cm":
            return fnValidHeightinCM(height)
        elif hType == "in":
            return fnValidHeightinInches(height)
        else:
            return False
    except:
        return False

def fnValidHeightinInches(height):
    if height >= 59 and height <= 76:
        return True
    else:
        return False

def fnValidHeightinCM(height):
    if height >= 150 and height <= 193:
        return True
    else:
        return False

def fnValidHair(value):
    charRe = re.compile(r'[^a-f0-9]')

    if value[0] == '#':
        if len(value[1:]) == 6:
            test = charRe.search(value[1:])
            return not bool(test)
        else:
            return False
    else:
        return False

def fnValidEye(value):
    vValidEyeCol = ['amb','blu','brn','gry','grn','hzl','oth']

    if value in vValidEyeCol:
        return True
    else:
        return False

def fnValidPassportID(value):
    vValidDigits = re.compile(r'[^0-9]')

    if len(value) == 9:
        test = vValidDigits.search(value)
        return not bool(test)
    else:
        return False

for entry in raw_batch_file:
    document = fnCreateDocumentDictionary(entry)
    print(document)
    if fnValidatePassport(document,passport_fields,passport_optional_fields):
        print('Valid passport')
        valid_passports += 1
    else:
        print('Invalid passport')

print(valid_passports)
