def readFile(file):
    temp = []
    f = open(file, 'r')
    data = f.readlines()
    f.close()
    for i in data:
        i = i.strip()
        row = i.split(',')
        row = [float(x) for x in row]
        temp.append(row)
    return temp

def createOutput(list):
    tempStr = ''
    for i in list:
        for j in range(len(i)-1):
            tempStr += str(i[j]) + ','
        tempStr += str(int(i[-1])) + '\n'
    f = open('testoutput.txt', 'w')
    f.write(tempStr)
    print("Finished creating output.txt")
    f.close()
        