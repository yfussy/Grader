operator = input()
n = int(input())
box = []
for i in range(n):
    box.append(list(input().strip()))
if all(len(box[0]) == len(layer) for layer in box):
    match operator:
        case "flip":
            flip = []
            for i in range(n):
                fLayer = []
                for j in range(1, len(box[0])+1):
                    fLayer.append(box[i][-j])
                flip.append(fLayer)
            for layer in flip:
                print(''.join(layer))

        case _:
            operator = int(operator)
            rotate = []
            for i in range(operator//90):
                for j in range(len(box[0])):
                    rLayer = []
                    for k in range(1, len(box)+1):
                        rLayer.append(box[-k][j])
                    rotate.append(rLayer)
                box = rotate
                rotate = []
            for layer in box:
                print(''.join(layer))
else:
    print("Invalid size")