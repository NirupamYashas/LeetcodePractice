'''
Example:  Input arr = [100,80,60,70,60,75,85]; Output arr = [1,1,1,2,1,4,6]
'''

def ConsequtiveSmallerOrEqual(arr):

    stack = []
    size = len(arr)
    Output = [1]*size

    for i in range(size):

        if len(stack) == 0:
            Output[i] = 1

        elif len(stack) > 0 and stack[-1][0] <= arr[i]:
            while len(stack)>0 and stack[-1][0] <= arr[i]:
                stack.pop()
            if stack:
                Output[i] = i - stack[-1][1]
        
        elif len(stack) > 0 and stack[-1][0] > arr[i]:
            Output[i] = i - stack[-1][1]

        stack.append([arr[i],i])

    return Output

Arr = [100,80,60,70,60,75,85]
print(ConsequtiveSmallerOrEqual(Arr))


