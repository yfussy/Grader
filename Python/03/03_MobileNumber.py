number = input()

if number[:2] == "06" or number[:2] == "08" or number[:2] == "09":
    if len(number) == 10:
        print("Mobile number")
    else:
        print("Not a mobile number")
else:
    print("Not a mobile number")