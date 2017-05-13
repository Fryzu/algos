#My first Python program, quicksort and some tests

import random

#---------------------------------------------------------------------

#Generating test list
def generateList(numberTable):
    size = random.randrange(1, 1000)
    for x in range(0, size):
        numberTable.append(random.randrange(-1000000, 1000000))
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

def getPivot(left, right):

    pivot = (left+right)/2

    return pivot

def swap(numberTable, x, y):

    tmp =  numberTable[y]
    numberTable[y] = numberTable[x]
    numberTable[x] = tmp

    return

def quicksort(numberTable, left, right):

    if left >= right:
        return
    pivot = numberTable[getPivot(left, right)]

    l = left - 1
    r = right + 1

    while True:

        while True:
            l += 1
            if numberTable[l] >= pivot:
                break
        while True:
            r -= 1
            if numberTable[r] <= pivot:
                break
        if l <= r:
            swap(numberTable, l, r)
        else:
            break
    
    if r > left:
        quicksort(numberTable, left, r)
    if l < right:
        quicksort(numberTable, l, right)

#---------------------------------------------------------------------

hababa = []
generateList(hababa)
print(hababa)
quicksort(hababa, 0, len(hababa) - 1)
testIfSorted(hababa)
