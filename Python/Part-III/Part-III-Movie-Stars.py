n = int(input())
starring = {}
for _ in range(n):
    movie, act1, act2 = input().split(', ')
    if act1 in starring:
        starring[act1].append(movie)
    else:
        starring[act1] = [movie]
    if act2 in starring:
        starring[act2].append(movie)
    else:
        starring[act2] = [movie]
stars = [e.strip() for e in input().split(', ')]
for star in stars:
    if star in starring:
        print(star, "->", ", ".join(starring[star]))
    else:
        print(star, "-> Not found")