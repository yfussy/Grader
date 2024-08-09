vector1 = list(map(float, (input()[1:-1].split(', '))))
vector2 = list(map(float, (input()[1:-1].split(', '))))

ans = list(map(sum, zip(vector1, vector2)))

print(f'{vector1} + {vector2} = {ans}')