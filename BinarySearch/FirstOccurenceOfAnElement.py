def FirstOccurence(Arr,num):

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

Arr = [2,4,10,10,10,18,20]
print(FirstOccurence(Arr,10))
        