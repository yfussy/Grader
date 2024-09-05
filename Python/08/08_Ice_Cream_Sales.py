n = int(input())
ic = {}
for _ in range(n):
    name, price = input().split()
    ic[name] = int(price)

m = int(input())
sales = {}
for _ in range(m):
    name, amount = input().split()
    if name in ic.keys():
        amount = int(amount) * ic[name]
        sales[name] = amount if name not in sales else (sales[name] + amount)
if sales:
    print(f'Total ice cream sales: {float(sum(sales.values()))}')
    topPrice = max(sales.values())
    top = sorted([name for name, price in sales.items() if price == topPrice])
    print(f'Top sales: {", ".join(top)}')
else:
    print("No ice cream sales")