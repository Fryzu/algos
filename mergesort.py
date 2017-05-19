#Mergesort algorythm

import random

#---------------------------------------------------------------------

#Generating test list
def generateList(numberTable):
    size = random.randrange(1, 10000)
    for x in range(0, size):
        numberTable.append(random.randrange(-1000, 1000))
    return

#Sort test
def testIfSorted(numberTable):

    testList = []
    for x in range(0, len(numberTable)):
        testList.append(numberTable[x])
    testList.sort()

    print(numberTable)
    print(testList)

    result = 1

    for x in range(0, len(numberTable)):
        if testList == numberTable:
            print('OK')
        else:
            print('WRONG')
            result = 0

    return result

#---------------------------------------------------------------------

def merge(numberTable, center, left, right):
    tmpTable = []
    firstIterator = left
    secondIterator = center + 1

    #while two parts are not empty
    while (firstIterator <= center) and (secondIterator <= right):

        if numberTable[firstIterator] <= numberTable[secondIterator]:
            tmpTable.append(numberTable[firstIterator])
            firstIterator += 1
        else:
            tmpTable.append(numberTable[secondIterator])
            secondIterator += 1
    
    #one part is empty
    if firstIterator <= center:
        while firstIterator <= center:
            tmpTable.append(numberTable[firstIterator])
            firstIterator += 1
    else:
        while secondIterator <= right:
            tmpTable.append(numberTable[secondIterator])
            secondIterator += 1

    #rewriting list
    k = 0
    for x in range(left, right+1):
        numberTable[x] = tmpTable[k]
        k += 1
        
    return

def mergeSort(numberTable, left, right):
    if left != right:
        
        center = (left + right)/2
        mergeSort(numberTable, left, center)
        mergeSort(numberTable, center + 1, right)
        merge(numberTable, center, left, right)
        
    else:
        return

#---------------------------------------------------------------------
#starting test
if __name__ == '__main__':
    #starting sort test
    testList = []
    generateList(testList)
    mergeSort(testList, 0, len(testList) - 1)
    if testIfSorted(testList) == 1:
        print('test passed')
    else:
        print('test failed')