# missing 9, 10 testcases :
#   - line of operations do not match with amount of operation given at first

n = int(input())
bidder = []
prodBid = {}
for _ in range(n):
    op, name, *data = input().split()

    match op:
        case 'B':
            prod, price = data
            price = int(price)
            if name not in bidder:
                bidder.append(name)
            
            if prod in prodBid:
                currentBid = prodBid[prod]
                if currentBid:
                    if price < currentBid[-1][1]:
                        currentBid.append((name,price))
                    else:
                        for i in range(len(currentBid)):
                            if price > currentBid[i][1]:
                                currentBid.insert(i, (name,price))
                                break
                else:
                    prodBid[prod] = [(name,price)]
            else:
                prodBid[prod] = [(name,price)]
        case 'W':
            prod = data[0]
            currentBid = prodBid[prod]
            for bid in currentBid[:]:
                if name in bid:
                    currentBid.remove(bid)
        case _:
            continue

prodBid = {prod:bid[0] for prod,bid in sorted(prodBid.items(),key=lambda x: x[0]) if bid}
bidder = {name: [0, []] for name in sorted(bidder)}

for prod, bid in prodBid.items():
    name, price = bid
    bidder[name][0] += price
    bidder[name][1].append(prod)

for name, bid in bidder.items():
    money, prod = bid
    bidded = f" -> {' '.join(prod)}" if prod else ''
    print(f"{name}: ${money}{bidded}")