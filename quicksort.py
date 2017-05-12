#My first Python program, quicksort and some tests

#There is a problem when two same number meet in comparison, they keep swaping

import random

#---------------------------------------------------------------------

#Generating test list
def generateList(numberTable):
    size = random.randrange(1, 10)
    for x in range(0, size):
        numberTable.append(random.randrange(-10, 10))
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

#The big test
        

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
    
    l = left
    r = right

    if l >= r:
        return
    
    pivot = numberTable[getPivot(l, r)]

    while l < r:
        while numberTable[l] < pivot:
            l += 1
        while numberTable[r] > pivot:
            r -= 1
        swap(numberTable, l, r)

    quicksort(numberTable, left, r-1)
    quicksort(numberTable, l+1, right)

#---------------------------------------------------------------------

hababa = []
generateList(hababa)
print(hababa)
quicksort(hababa, 0, len(hababa) - 1)
testIfSorted(hababa)
