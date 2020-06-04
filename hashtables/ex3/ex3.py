def intersection(arrays):
    storage = dict()
    result = []
    for index, arr in enumerate(arrays): #a listing of all of the elements of a set
        for v in arr:
            if storage.get(v) is not None and index > 0: #.get returns value from storage
                storage[v] += 1 # we either add on to an existing value indicating it's found in more than one arr
            elif storage.get(v) is None and index == 0:
                storage[v] = 1 #or we start a new spot for the first arr's value
            else:
                continue # if a new num in a following arr that wasnt seen in previous arr, skip it as it cannot be in common
    for values in storage:
        if storage[values] == len(arrays):
            result.append(values) # if val is present in all subarrays, add to result list
    return result

print(intersection([[1,2,3], [1,3,5],[5,4,3]]))
print(intersection([[1,2,3], [1,3,5],[1,4,3], [1,3,9], [4,1,3]]))
if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
