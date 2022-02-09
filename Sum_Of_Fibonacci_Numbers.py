# riddle from InterviewBit
import math
def fibsum(A):
    if numinFibonacci(A):
        return 1
    fiblist = buildlistfib(A)
    rest = A - int(fiblist[-1])
    if numinFibonacci(rest): return 2
    return 1 + fibsum(rest)

def numinFibonacci(num):
    option = 5*(num*num)+4
    if isperfectsquare(option): return True
    else:
        option = option - 8
        if isperfectsquare(option): return True
    return False

def isperfectsquare(number):
    x = int(math.sqrt(number))
    return x*x == number

def buildlistfib(lim):
    fiblist: list[int] = [0, 1]
    i = 2
    x = 1
    while x < lim:
        fiblist.append(x)
        i += 1
        x = fiblist[i-1] + fiblist[i-2]
    return fiblist

testnum = 5
print("fibs-um of ", testnum, " is ", fibsum(testnum))
