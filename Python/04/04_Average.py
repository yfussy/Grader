nums = []
while True:
    num = input()
    if num == 'q':
        break
    nums.append(float(num))

if not nums:
    print('No Data')
else:
    print(round(sum(nums)/len(nums), 2))