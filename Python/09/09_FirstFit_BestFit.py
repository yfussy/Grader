def first_fit(L, e):
    for nums in L:
        if sum(nums) + e <= 100:
            nums.append(e)
            return
    L.append([e])

def best_fit(L, e):
    leftMax = 100
    maxIndex = 0
    for nums in L:
        if sum(nums) + e <= 100:
            left = 100 - sum(nums)
            if left < leftMax:
                maxIndex = L.index(nums)
                leftMax = left
    if leftMax < 100:
        L[maxIndex].append(e)
    else:
        L.append([e])

def partition_FF(D):
    l = []
    for num in D:
        first_fit(l, num)
    return l

def partition_BF(D):
    l = [[D[0]]]
    for num in D[1:]:
        best_fit(l, num)
    return l

exec(input().strip())