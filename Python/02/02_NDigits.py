num = input()
length = int(input())

if length == max(len(num), length):
    num = '0'*(length - len(num)) + num

print(num)