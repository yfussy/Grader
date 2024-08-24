n = int(input())
nums = []
for i in range(n):
    num = int(input())
    nums.append(num)
num = list(map(int, input().split()))
nums += num
while True:
    num = int(input())
    if num == -1:
        break
    nums.append(num)
numList = []
swap = 1
for num in nums:
    if swap == 1:
        numList.append(num)
        swap *= -1
    else:
        numList.insert(0, num)
        swap *= -1
print(numList)