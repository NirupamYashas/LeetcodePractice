'''
Example:  Input arr = [[0,1,1,0],[1,1,1,1],[1,1,1,1],[1,1,0,0]]; Output = 8 (MAX AREA RECTANGLE = area of 2nd and 3rd row of matrix)
'''

def MaxAreaRecInBinaryMatrix(Arr):

    n = len(Arr)
    m = len(Arr[0])
    Vector = []

    for j in range(m):
        Vector.append(Arr[0][j])
    
    mx = MaximumAreaHistogram(Vector)

    for i in range(1,n):
        for j in range(m):
            if(Arr[i][j] == 0):
                Vector[j] = 0
            else:
                Vector[j] = Vector[j] + Arr[i][j]
        
        mx = max(mx,MaximumAreaHistogram(Vector))
    return mx

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

Arr = [[0,1,1,0],[1,1,1,1],[1,1,1,1],[1,1,0,0]]
print(MaxAreaRecInBinaryMatrix(Arr))
