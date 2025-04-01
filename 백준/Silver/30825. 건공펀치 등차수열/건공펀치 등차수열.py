N,K = map(int,input().split())

arr = list(map(int,input().split()))

cnt = 0

start = arr[0]

for idx in range(N):
    if arr[idx] <= start+idx*K:
        cnt += start+idx*K - arr[idx]
    else:
        cnt += (arr[idx] - (start + idx*K)) * (idx)
        start += arr[idx] - (start + idx*K)

print(cnt)