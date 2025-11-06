def binSearchSqrt(target, A):
    l = 0
    r = len(A) - 1  # Fixed: use the last index of the array
    
    while l <= r:
        middle = (l + r) // 2
        if A[middle] ** 2 > target:  # Fixed: compare with target, not A[target]
            r = middle - 1
        elif A[middle] ** 2 < target:
            l = middle + 1
        else:
            return middle
    return r

A = [int(x) for x in input().split()]
target = int(input())
print(A[binSearchSqrt(target, A)])
