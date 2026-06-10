1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
from collections import deque

def solution(m, n, h, w, drops):
    INF = len(drops) + 1

    time = [[INF] * n for _ in range(m)]
    for i, (r, c) in enumerate(drops):
        time[r][c] = i + 1

    # 가로 슬라이딩 최소
    row_min = [[0] * (n - w + 1) for _ in range(m)]

    for r in range(m):
        dq = deque()
        for c in range(n):

            while dq and time[r][dq[-1]] >= time[r][c]:
                dq.pop()

            dq.append(c)

            if dq[0] <= c - w:
                dq.popleft()

            if c >= w - 1:
                row_min[r][c - w + 1] = time[r][dq[0]]

    best = -1
    ans = (0, 0)

    # 세로 슬라이딩
    for c in range(n - w + 1):
        dq = deque()

        for r in range(m):

            while dq and row_min[dq[-1]][c] >= row_min[r][c]:
                dq.pop()

            dq.append(r)

            if dq[0] <= r - h:
                dq.popleft()

            if r >= h - 1:

                val = row_min[dq[0]][c]
                top = r - h + 1

                # 핵심 수정 (tie-breaking)
                if val > best or (val == best and (top, c) < ans):
                    best = val
                    ans = (top, c)

    return list(ans)