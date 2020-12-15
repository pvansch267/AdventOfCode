import itertools
import numpy
puzzle_data = open("C:\\Users\Paul\Documents\\Advent of Code\\Day 1\\data.txt","r")
content = puzzle_data.readlines()
content = [int(x.strip()) for x in content]
target = 2020
def fnSumofXValues(target,XValues):
    for numbers in itertools.combinations(content,XValues):
        if sum(numbers) == target:
            for i in numbers:
                print(i)
            print(numpy.prod(numbers))
fnSumofXValues(target,3)