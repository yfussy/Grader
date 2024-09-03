def total(pocket):
    money = 0
    for bank, amount in pocket.items():
        money += bank * amount

    return money

def take(pocket, money_in):
    pocket.update({key: sum([pocket[key], money_in[key]]) if key in money_in else pocket[key] for key in pocket})
    pocket.update({key: money_in[key] for key in money_in if key not in pocket})
    return pocket

def pay(pocket, amt):
    if amt > total(pocket):
        return {}
    pay = {}
    for bank in pocket:
        payable = min(amt//bank, pocket[bank])
        if payable > 0:
            pay.update({bank: -payable})
            amt -= bank * payable
    if amt > 0:
        return {}
    take(pocket, pay)
    pay.update({key: abs(pay[key]) for key in pay})
    return pay

exec(input().strip())