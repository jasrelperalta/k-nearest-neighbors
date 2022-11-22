def readFile(file):
    temp = []
    f = open(file, 'r')
    data = f.readlines()
    for i in data:
        i = i.strip()
        row = i.split(',')
        row = [float(x) for x in row]
        temp.append(row)
    return temp