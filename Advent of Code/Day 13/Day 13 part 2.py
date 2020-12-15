from functools import reduce

# Open the file
with open("C:\\Users\\Paul\\Documents\\Advent of Code\\Day 13\\data.txt",'r') as raw_cypher_data:
    content = [line.strip() for line in raw_cypher_data.readlines()]

lstBusList = content[1].split(',')

def fnGetRemainderList(lstBusList):
    lstRemainder = []
    vBusCount = 0

    for bus in lstBusList:
        if bus != 'x':
            if vBusCount == 0:
                lstRemainder.append(vBusCount)
            else:
                lstRemainder.append(int(bus) - vBusCount)
            vBusCount += 1
        else:
            vBusCount += 1

    return lstRemainder

lstRemainder = fnGetRemainderList(lstBusList)

lstBusList = list(filter(lambda  a : a != 'x', lstBusList))
lstBusList = [int(x) for x in lstBusList]

print(lstBusList)
print(lstRemainder)


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

test_1 = [7,13,59,31,19]
test_2 = [0,12,55,25,12]

print(chinese_remainder(lstBusList,lstRemainder))