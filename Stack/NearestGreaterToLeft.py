'''
Example:  Input arr = [1,3,2,4]; Output arr = [-1,-1,3,-1]
'''

def NearestGreaterToLeft(arr):

    stack = []
    size = len(arr)
    output = [-1]*size

    for i in range(size):

        while stack and stack[-1] <= arr[i]:
            stack.pop()

        if stack:
            output[i] = stack[-1]
        
        stack.append(arr[i])

    return output

Arr = [1,3,2,4]
print(NearestGreaterToLeft(Arr))