import fileHandler
import compute


# note: clean every iteration tas use insert

trainingData = fileHandler.readFile('data/diabetes.csv')
inputData = fileHandler.readFile('data/input.in')

# trainingData = fileHandler.readFile('basic.txt')
# inputData = [[4,4]]
k = 5

# for row in trainingData:
#     # print(row)

res = []
for row in inputData:
    neighbors = compute.computeDistance(row, trainingData, k)
    row.append(compute.classifyNeighbors(neighbors))
    compute.cleanData(trainingData)
    trainingData.append(row)
    res.append(row)

fileHandler.createOutput(res)