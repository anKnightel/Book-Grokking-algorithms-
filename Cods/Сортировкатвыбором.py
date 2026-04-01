def findSmalest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            smallest_index = i
    
    return smallest_index


def selectionSort(array):
    result = []
    copy = list(array)

    for i in range(len(copy)):
        smal = findSmalest(copy)
        result.append(copy.pop(smal))

    return result


print(selectionSort([8, 45, 23, 2, 0, 75, 34]))
# Аналог
#arr.sort()