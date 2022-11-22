import fileHandler
import compute


trainingData = fileHandler.readFile('data/diabetes.csv')
inputData = fileHandler.readFile('data/input.in')

# trainingData = fileHandler.readFile('data02/fruits.csv')
# inputData = fileHandler.readFile('data02/input.in')


k = 5


res = []
for row in inputData:
    # get neighbors of row
    neighbors = compute.computeDistance(row, trainingData, k)

    # add the classification of row to the row
    row.append(float(compute.classifyNeighbors(neighbors)))
    
    # clean the training data since distance value was appended to the list
    compute.cleanData(trainingData)
    
    # added the newly made row
    trainingData.append(row)
    
    # add the row to the final result for output
    res.append(row)

# create output.txt file
fileHandler.createOutput(res)