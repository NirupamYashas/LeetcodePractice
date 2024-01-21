'''
Example:  Input arr = [3,0,0,2,0,4]; Output = 10 (WATER FILLED AREA = 4*3)

Logic = Summation (Water[i])

Water[i] = Water on Top of each Tower

Water[i] = min( MXL[i], MXR[i]) - arr[i]

where MXL = Maximum of left array at any particular index i
      MXR = Maximum of right array at any particular index i
'''


def RainWaterTrapping(arr):

    size = len(arr)
    MXLArr = [-1]*size
    MXRArr = [-1]*size
    Water = [-1]*size

    maxl = arr[0]
    for i in range(size):
        maxl = max(maxl,arr[i])
        MXLArr[i] = maxl 

    maxr = arr[size-1]
    for i in range(size-1,-1,-1):
        maxr = max(maxr,arr[i])
        MXRArr[i] = maxr

    for i in range(size):
        Water[i] = min(MXLArr[i],MXRArr[i]) - arr[i]

    return sum(Water)
    

Arr = [3,0,0,2,0,4]
print(RainWaterTrapping(Arr))