N = int(input())
arr = list(map(int,input().split()))
arr.sort()

ans = 0

for k in range(N):
    target = arr[k]
    i = 0
    j = N-1
    while i<j:
        if i==k:
            i+=1
            continue
        if j==k:
            j-=1
            continue
        result = arr[i] + arr[j]
        if result == target:
            ans += 1
            break
        if result > target:
            j -= 1
        else:
            i += 1

print(ans)