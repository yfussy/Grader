num = input()

if num[0] == '-':
    print("negative")
elif num == '0':
    print("zero")
else:
    print("positive")

if int(num) % 2 == 0:
    print("even")
else:
    print("odd")