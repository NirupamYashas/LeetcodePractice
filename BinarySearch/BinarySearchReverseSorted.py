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
            start = mid + 1
            
        elif element > Arr[mid]:
            end = mid - 1

    return -1

Arr = [8,7,6,5,4,3,2,1]
print(BinarySearch(Arr,2))