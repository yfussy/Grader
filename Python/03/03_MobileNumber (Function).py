def is_mobile_number(number):
    if number[:2] == "06" or number[:2] == "08" or number[:2] == "09":
        if len(number) == 10:
            return True
    return False

exec(input())