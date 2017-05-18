#counting sort

import random

#---------------------------------------------------------------------

#test list generator

rangeStart = -1000000
rangeEnd = 1000000

#generating test list
def generateList(numberTable):
    size = random.randrange(1, 1000)
    for x in range(0, size):
        numberTable.append(random.randrange(rangeStart, rangeEnd))
    return

#Sort test
def testIfSorted(numberTable):

    testList = []
    for x in range(0, len(numberTable)):
        testList.append(numberTable[x])
    testList.sort()

    print(numberTable)
    print(testList)

    for x in range(0, len(numberTable)):
        if testList == numberTable:
            print('OK')
        else:
            print('WRONG')
    return

#---------------------------------------------------------------------

def countingSort(numberTable):
    
    #creating auxiliary table and filling it with zeros
    indexTable = []
    for x in range(rangeStart, rangeEnd + 1):
        indexTable.append(0)

    #counting
    for x in range(0, len(numberTable)):
        indexTable[numberTable[x]] += 1

    #rewriting the table
    i = 0
    for x in range(0, len(indexTable)):
        while indexTable[x] > 0:
            numberTable[i] = x
            i += 1
            indexTable[x] -= 1

#---------------------------------------------------------------------

testList = []
generateList(testList)
countingSort(testList)
testIfSorted(testList)
