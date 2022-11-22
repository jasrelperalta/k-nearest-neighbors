import math, statistics

def sortFn(dataList):                                           # function used in sorting
    return dataList[-1]

def computeDistance(row, data, k):
    tempList = []
    for trainRow in data:
        tempSum = 0
        tempRow = trainRow
        for i in range(len(row)):                               # classification not included
            tempSum += (row[i] - tempRow[i])**2
        tempSum = math.sqrt(tempSum)
        tempRow.append(tempSum)
        if len(tempList) < k:
            tempList.append(tempRow)
        else:
            for i in range(len(tempList)-1, -1, -1):            # descending order
                if tempList[i][-1] > tempRow[-1]:
                    tempList.remove(tempList[i])
                    tempList.append(tempRow)
                    tempList.sort(key=sortFn)                   # sorts the list based on the last index
                    break                                       # idea from https://www.freecodecamp.org/news/python-list-sorting-how-to-order-lists-in-python/
                    

    return tempList

def classifyNeighbors(list):
    classes = []
    for i in list:
        classes.append(int(i[-2]))                              # append their classifications
    
    mulClassification = statistics.multimode(classes)           # instance wherein there are two modes
    classifiction = statistics.mode(classes)                    # single mode


    if len(mulClassification) == 1:
        return classifiction
    else:
        return breakTie(list, mulClassification)

def breakTie(list, nums):
    list.sort(key=sortFn)                                       # list the neighbors by their distance
    for i in list:                                              # start from closest
        if i[-2] in nums:                                       # item is classified as one from the ties, return it
            return i[-2]


def cleanData(data):
    for row in data:
        row.pop()                                               # remove the distance value
    return data