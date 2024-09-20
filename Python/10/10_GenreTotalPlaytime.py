n = int(input())
genres = {}
for _ in range(n):
    name, artist, genre, time = input().split(', ')
    h, m = time.split(':')
    m = int(m) + int(h)*60
    if genre not in genres:
        genres[genre] = m
    else:
        genres[genre] += m
for genre, time in sorted(genres.items(), key=lambda x: x[1], reverse=True)[:3]:
    h = time//60
    m = time - h*60
    if m < 10:
        m = '0' + str(m)
    print(f'{genre} --> {h}:{m}')