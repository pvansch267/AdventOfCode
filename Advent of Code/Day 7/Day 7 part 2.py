
raw_batch_data = open("C:\\Users\\Paul\\Documents\\Advent of Code\\Day 7\\test_data.txt","r")

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
            value = {t[2:]:int(t[0]) for t in tmpValue.split(', ')}
        else:
            value = {}
        dict_1 = {key:value}
        dictBags.update(dict_1)
    return dictBags

fnCreateParentBags(content)

master_list = []
prod_list = []

def fnContainsShinyGold(bagName):
    parent = bagName
    vBagContents = dictBags[bagName]

    for children,qty in vBagContents.items():
        if children == 'shiny gold bag':
            master_list.append(parent)
            return True
        else:
            if fnContainsShinyGold(children):
                master_list.append(parent)
                return True
            
    return False

def fnPartOne():
    for key,value in dictBags.items():
        fnContainsShinyGold(key)
    distinct_master_list = set(master_list)
    print(len(distinct_master_list))


bagcount = 1
vTotalQty = 0

def fnPartTwo(bagName, bagcount,vTotalQty):
    parent = bagName
    print(parent)
    vBagContents = dictBags[bagName]

    print(vBagContents)

    prod_list.append(bagcount)
#    vSumChildren = sum(vBagContents.values())
    print('Total: ',vTotalQty)
    print('BagCount: ',bagcount)
#    print('vSumChildren: ', vSumChildren)
#    vTotalQty = vTotalQty + (bagcount * vSumChildren)
#    print('Total: ',vTotalQty)   
#    test = reduce(set.union,vBagContents.values())

    for children,qty in vBagContents.items():
        bagcount = qty
        vChild = children
        vTotalQty += qty * (fnPartTwo(vChild,bagcount,vTotalQty) + 1)
#        vTotalQty = fnPartTwo(vChild,bagcount,vTotalQty)
    
    return vTotalQty
    


print(fnPartTwo('shiny gold bag', bagcount,vTotalQty))
#print(prod_list)
#print(sum(prod_list)-1)