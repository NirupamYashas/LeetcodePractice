'''
Example:  Input Order Arr = [18, 19, 29, 15, 16]; Implement GetMinElement, Push and Pop Methods, 
which should work at any particular point when called in between the order.
'''

def Pop():
    if len(Stack) == 0:
        return -1
    ans = Stack[-1]
    Stack.pop()
    if SuppportingStack[-1] == ans:
        SuppportingStack.pop()
    return ans

def Push(num):
    Stack.append(num)
    if len(SuppportingStack) == 0 or SuppportingStack[-1] >= num:
        SuppportingStack.append(num)
    return

def GetMinElement():
    if len(SuppportingStack) == 0:
        return -1
    return SuppportingStack[-1]

Stack = []
SuppportingStack = []


Arr = [18, 19, 29, 15, 16]
Push(Arr[0])
Push(Arr[1])
Push(Arr[2])
print(GetMinElement()) #should return 18
Push(Arr[3])
print(GetMinElement()) #should return 15
print(Pop()) #should return 15
print(GetMinElement()) #should return 18
Push(Arr[4])
print(GetMinElement()) #should return 16
print(Pop()) #should return 16
print(Pop()) #should return 29
print(Pop()) #should return 19
print(Pop()) #should return 18







