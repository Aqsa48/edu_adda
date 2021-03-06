## Using Basic Approach
global maximum

def _lis(arr, n ):
    global maximum
    if n == 1 :
        return 1
    maxEndingHere = 1
    for i in xrange(1, n):
        res = _lis(arr, i)
        if arr[i-1] < arr[n-1] and res + 1 > maxEndingHere:
            maxEndingHere = res + 1
    maximum = max(maximum, maxEndingHere)
    return maxEndingHere

def lis(arr):
    global maximum
    n = len(arr)
    maximum = 1
    _lis(arr, n)
    return maximum

## Using Dynamic Programming
def lis(arr):
    n = len(arr)
    lis = [1]*n
    for i in range (1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 :
                lis[i] = lis[j]+1
    maximum = 0
    for i in range(n):
        maximum = max(maximum, lis[i])

    return maximum
