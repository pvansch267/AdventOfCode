
raw_batch_data = open("C:\\Users\\Paul\\Documents\\Advent of Code\\Day 7\\data.txt","r")
                      
content = raw_batch_data.read().strip().split('\n')

dictBags = {}

count = 0

# Create Master Rules List
def fnCreateParentBags(content):
    for line in content:
        line = line.replace('bags','bag').replace('.','')
        key = line.split(' contain ')[0]
        tmpValue = line.split(' contain ')[1]
        if tmpValue != 'no other bag':
            value = {t[2:]:t[0] for t in tmpValue.split(', ')}
        else:
            value = {}
        dict_1 = {key:value}
        dictBags.update(dict_1)
    return dictBags

fnCreateParentBags(content)

#for key, value in dictBags.items():
#    print(key,value)

master_list = []

def fnContainsShinyGold(bagName):
    parent = bagName
#    print('Parent:', parent)
    vBagContents = dictBags[bagName]
#    print('Children', vBagContents)

    for children,qty in vBagContents.items():
        if children == 'shiny gold bag':
#            if parent not in master_list:
            master_list.append(parent)
            return True
        else:
            if fnContainsShinyGold(children):
#                if parent not in master_list:
                master_list.append(parent)
                return True
            
    return False

for key,value in dictBags.items():
    count += 1
    fnContainsShinyGold(key)

#print(count)
distinct_master_list = set(master_list)
print(len(distinct_master_list))
