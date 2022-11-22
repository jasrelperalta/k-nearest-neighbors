import math

def sortFn(dataList):                                           # function used in sorting
    return dataList[-1]

def computeDistance(row, data, k):
    tempList = []
    for trainRow in data:
        tempSum = 0
        tempRow = trainRow
        for i in range(len(row)):                               # classification not included
            # print(row[i], trainRow[i])
            tempSum += (row[i] - tempRow[i])**2
        tempSum = math.sqrt(tempSum)
        # print(tempRow, tempSum)
        tempRow.append(tempSum)
        if len(tempList) < k:
            tempList.append(tempRow)
        else:
            for i in range(len(tempList)-1, -1, -1):            # descending order
                if tempList[i][-1] > tempRow[-1]:
                    tempList.remove(tempList[i])
                    tempList.append(tempRow)
                    tempList.sort(key=sortFn)                   # sorts the list based on the last index
                                                                # idea from https://www.freecodecamp.org/news/python-list-sorting-how-to-order-lists-in-python/
                    # for i in (tempList):
                    #     print(i)
                    # print('\n\n')
                    break

    return tempList

def classifyNeighbors(list):
    xcount = 0
    ycount = 0
    for i in list:
        if i[-2] == 0:
            xcount += 1
        else:
            ycount += 1

    if xcount > ycount:
        return 0
    else:
        return 1

def cleanData(data):
    for row in data:
        row.pop()
    return data