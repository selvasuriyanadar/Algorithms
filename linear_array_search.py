def searchByLinearAlgorithm(data, search):
    index = 0
    for d in data:
        if d == search:
            return index
        index+=1
    return -1

data = [1, 4, 7, 9, 11, 3]

search = 1

print(searchByLinearAlgorithm(data, search))
