def CountOfElementInSortedArray(Arr,num):

    first_occurence = BSFO(Arr,num)
    last_occurence = BSLO(Arr,num)

    return (last_occurence - first_occurence) + 1

def BSFO(Arr,num):
    size = len(Arr)
    start = 0
    end = size - 1
    while start <= end:
        mid = start + (end - start) // 2
        if num == Arr[mid]:
            res = mid
            end = mid - 1
        elif num < Arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return res

def BSLO(Arr,num):
    size = len(Arr)
    start = 0
    end = size - 1
    while start <= end:
        mid = start + (end - start) // 2
        if num == Arr[mid]:
            res = mid
            start = mid + 1
        elif num < Arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return res

Arr = [2,4,10,10,10,18,20]
print(CountOfElementInSortedArray(Arr,10))