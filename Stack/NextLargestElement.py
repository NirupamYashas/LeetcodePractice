'''
Example:  Input arr = [1,3,2,4]; Output arr = [3,4,4,-1]
'''
from collections import deque
def NextLargertElement(arr):

    stack = []
    size = len(arr)
    output = [-1]*size

    for i in range(size-1,-1,-1):

        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            output[i] = stack[-1]

        stack.append(arr[i])  

    return output

Arr = [1,3,2,4]
print(NextLargertElement(Arr))


    