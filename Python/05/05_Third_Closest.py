n = int(input())
coordinates = []
for i in range(1, n+1):
    coordinateX, coordinateY = list(map(float, input().split()))
    distance = ((coordinateX**2) + (coordinateY**2))**0.5
    coordinate = [distance, i, coordinateX, coordinateY]
    coordinates.append(coordinate)
coordinates.sort()
print(f'#{coordinates[2][1]}: ({coordinates[2][2]}, {coordinates[2][3]})')