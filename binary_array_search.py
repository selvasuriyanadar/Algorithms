import math

class SearchNotFound(Exception):
    pass

def _searchByBinaryAlgorithm(data, search, start_index=0):
    if len(data) == 0:
        raise SearchNotFound()

    index = math.ceil(len(data)/2) - 1
    if data[index] == search:
        return start_index + index
    if data[index] > search:
        return start_index + _searchByBinaryAlgorithm(data[:index], search)
    if data[index] < search:
        return start_index + _searchByBinaryAlgorithm(data[index+1:], search, index+1)

    raise Exception("The search has to be comparable with the data.")

def searchByBinaryAlgorithm(data, search):
    try:
        return _searchByBinaryAlgorithm(data, search)
    except SearchNotFound:
        return -1

data = [1, 4, 7, 9, 11, 13, 23, 26]

search = 12

print(searchByBinaryAlgorithm(data, search))
