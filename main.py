import fileHandler

trainingData = fileHandler.readFile('data/diabetes.csv')
inputData = fileHandler.readFile('data/input.in')

for row in trainingData:
    print(row)

print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx INPUTS xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
for row in inputData:
    print(row)