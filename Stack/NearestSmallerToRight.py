'''
Example:  Input arr = [4,5,2,10,8]; Output arr = [2,2,-1,8,-1]
'''

def NearestSmallerToRight(arr):

    stack = []
    size = len(arr)
    Output = [-1] * size

    for i in range(size-1,-1,-1):

        while stack and stack[-1] >= arr[i]:
            stack.pop()

        if stack:
            Output[i] = stack[-1]

        stack.append(arr[i])
    
    return Output

Arr = [4,5,2,10,8]
print(NearestSmallerToRight(Arr))