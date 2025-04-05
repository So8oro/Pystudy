N = int(input())
arr = [input() for _ in range(N)]
w,l = 0,0

for i in range(N):
    cnt = 0
    for j in range(N):
        if arr[i][j]=='.':
            cnt += 1
        else:
            if cnt>= 2:
                w += 1
            cnt = 0
    if cnt>=2:
        w += 1

for j in range(N):
    cnt = 0
    for i in range(N):
        if arr[i][j]=='.':
            cnt += 1
        else:
            if cnt >= 2:
                l += 1
            cnt = 0
    if cnt>=2:
        l += 1

print(w,l)