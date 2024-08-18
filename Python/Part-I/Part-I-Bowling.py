chart = input().strip()
n = int(input())
frame = 0
scores = []
lastFrame = []
newFrame = True
for i in range(len(chart)):
    score = chart[i]
    if frame != 9:
        if score == 'X':
            scores.append(10)
            if chart[i+1] == 'X':
                scores[-1] += 10
            else:
                scores[-1] += int(chart[i+1])

            if chart[i+2] == '/':
                scores[-1] += (10 - int(chart[i+1]))
            elif chart[i+2] == 'X':
                scores[-1] += 10
            else:
                scores[-1] += int(chart[i+2])
            newFrame = True
            frame += 1
        elif score == '/':
            scores[-1] += (10 - scores[-1])
            if chart[i+1] == 'X':
                scores[-1] += 10
            else:
                scores[-1] += int(chart[i+1])
            newFrame = True
            frame += 1
        elif newFrame:
            scores.append(int(score))
            newFrame = False
            continue
        else:
            scores[-1] += int(score)
            newFrame = True
            frame += 1
    else:
        if score == 'X':
            lastFrame.append(10) 
        elif score == '/':
            lastFrame.append(10 - lastFrame[-1])
        else:
            lastFrame.append(int(score)) 
    if frame == n:
        break
if lastFrame:
    scores.append(sum(lastFrame))
print(scores[-1] if (n > 0 and n <= 10) else sum(scores))