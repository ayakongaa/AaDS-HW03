def shellSort(arr):
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for curr in range(gap, n):
            mGap = curr
            while mGap >= gap and arr[mGap] < arr[mGap - gap]:
                arr[mGap], arr[mGap - gap] = arr[mGap - gap], arr[mGap]
                mGap -= gap
        gap //= 2
    
    return arr

def twoSum(data, target):
    cache = {}
    for i in range(len(data)):
        cache[data[i]] = i
    
    for i in range(len(data)):
        diff = target - data[i]
        if diff in cache and cache[diff] != i:
            return [data[i], diff]
    
    return []


m = [int(x) for x in input().split()]
tar = int(input())
shellSort(m)
print(twoSum(m, tar))
