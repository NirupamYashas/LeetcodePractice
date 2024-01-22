'''
Example:  Input Order Arr = [5, 3, 7, 8]; Implement GetMinElement, Push, Pop and Top Methods without using Extra Space, 
which should work at any particular point when called in between the order.
'''
Stack = []
minElement = -1

def GetMinElement():
    if len(Stack) == 0:
        return -1
    return minElement

def Push(num):
    global minElement
    if len(Stack) == 0:
        Stack.append(num)
        minElement = num
    else:
        if num >= minElement:
            Stack.append(num)
        elif num < minElement:
            flag = 2*num - minElement
            Stack.append(flag)
            minElement = num

    return

def Pop():
    global minElement
    if len(Stack) == 0:
        return -1
    else:
        if Stack[-1] >= minElement:
            ans = Stack[-1]
            Stack.pop()
        elif Stack[-1] < minElement:
            ans = minElement
            minElement = 2*minElement - Stack[-1]
            Stack.pop()

    return ans


def Top():
    if len(Stack) == 0:
        return -1
    else:
        if Stack[-1] >= minElement:
            return Stack[-1]
        else:
            return minElement


Arr = [5, 3, 7, 8]
Push(Arr[0])
print(GetMinElement()) #should print 5
Push(Arr[1])
print(GetMinElement()) #should print 3
print(Pop()) #should print 3
print(GetMinElement()) #should print 5
Push(Arr[2])
print(GetMinElement()) #should print 5
Push(Arr[3])
print(GetMinElement()) #should print 5
print(Pop()) #should print 8
print(GetMinElement()) #should print 5
print(Pop()) # should print 7
print(GetMinElement()) #should print 5
print(Pop()) #should print 5
print(GetMinElement()) #should print -1