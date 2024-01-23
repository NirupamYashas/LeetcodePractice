import math
def BinarySearch(Arr,element):

    size = len(Arr)
    start = 0
    end = size - 1
    mid = 0

    while start <= end:

        mid = start + (end - start) // 2

        if element == Arr[mid]:
            return mid
        
        elif element < Arr[mid]:
            end = mid - 1

        elif element > Arr[mid]:
            start = mid + 1

    return -1

Arr = [1,2,3,4,5,6,7,8]
print(BinarySearch(Arr,2))