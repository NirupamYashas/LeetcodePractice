'''
Example:  Input arr = [6,2,5,4,5,1,6]; Output = 12 (MAX AREA = 4*3)
'''

def MaximumAreaHistogram(Arr):

    size = len(Arr)
    AreaArr = [-1]*size
    WidthArr = [-1]*size

    NSLIndexArr = NearestSmallerToLeftIndex(Arr)
    NSRIndexArr = NearestSmallerToRightIndex(Arr)

    for i in range(size):
        WidthArr[i] = (NSRIndexArr[i] - NSLIndexArr[i]) - 1
        AreaArr[i] = WidthArr[i]*Arr[i]
    
    return max(AreaArr)

def NearestSmallerToLeftIndex(Arr):
    
    stack = []
    size = len(Arr)
    Output = [-1]*size

    for i in range(size):

        if len(stack) == 0:
            Output[i] = -1
        
        elif stack and stack[-1][0] >= Arr[i]:
            while stack and stack[-1][0] >= Arr[i]:
                stack.pop()
            if stack:
                Output[i] = stack[-1][1]

        elif stack and stack[-1][0] < Arr[i]:
            Output[i] = stack[-1][1]
        
        stack.append([Arr[i],i])

    return Output

def NearestSmallerToRightIndex(Arr):
    
    stack = []
    size = len(Arr)
    Output = [-1]*size

    for i in range(size-1,-1,-1):

        if len(stack) == 0:
            Output[i] = i+1
        
        elif stack and stack[-1][0] >= Arr[i]:
            while stack and stack[-1][0] >= Arr[i]:
                stack.pop()
            if stack:
                Output[i] = stack[-1][1]

        elif stack and stack[-1][0] < Arr[i]:
            Output[i] = stack[-1][1]
        
        stack.append([Arr[i],i])

    return Output

Arr = [6,2,5,4,5,1,6]
print(MaximumAreaHistogram(Arr))
