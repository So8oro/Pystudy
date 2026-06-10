from collections import deque

def get_sliding_window_min(arr, k):
    """
    1차원 배열 arr에서 크기가 k인 슬라이딩 윈도우의 최솟값들을 반환하는 함수.
    모노토닉 데크(Monotonic Deque)를 사용하여 O(N)의 시간 복잡도를 보장합니다.
    """
    res = []
    dq = deque()
    
    for i, val in enumerate(arr):
        # 1. 윈도우의 범위를 벗어난 인덱스 제거
        if dq and dq[0] < i - k + 1:
            dq.popleft()
            
        # 2. 데크의 끝에서부터, 현재 값(val)보다 크거나 같은 값들은 모두 제거
        #    (앞으로 윈도우 안에서 절대 최솟값이 될 수 없으므로 가지치기)
        while dq and arr[dq[-1]] >= val:
            dq.pop()
            
        # 3. 현재 인덱스 추가
        dq.append(i)
        
        # 4. 윈도우가 가득 차기 시작한 시점부터 맨 앞(최솟값)의 값을 결과에 추가
        if i >= k - 1:
            res.append(arr[dq[0]])
            
    return res

def solution(m, n, h, w, drops):
    # 1. 격자 초기화: 비가 내리지 않는 칸은 무한대(INF)로 설정
    INF = len(drops) + 1
    grid = [[INF] * n for _ in range(m)]
    
    # 빗방울이 떨어지는 시간을 1부터 시작하는 순서로 기록
    for idx, (r, c) in enumerate(drops):
        # 동일한 위치에 비가 여러 번 온다면 처음 맞은 시간이 기준이 됨
        if grid[r][c] == INF: 
            grid[r][c] = idx + 1
            
    # 2. 가로 방향(w) 슬라이딩 윈도우 최솟값 구하기
    row_mins = []
    for r in range(m):
        row_mins.append(get_sliding_window_min(grid[r], w))
        
    # 3. 세로 방향(h) 슬라이딩 윈도우 최솟값 구하기
    cols = n - w + 1
    rows = m - h + 1
    final_mins = [[0] * cols for _ in range(rows)]
    
    for c in range(cols):
        # 각 열(Column) 데이터를 1차원 배열로 추출하여 세로 최솟값 계산
        col_data = [row_mins[r][c] for r in range(m)]
        col_res = get_sliding_window_min(col_data, h)
        for r in range(rows):
            final_mins[r][c] = col_res[r]
            
    # 4. 가장 늦게 젖는(최솟값들 중 최댓값) 구역의 상단-좌측 좌표 찾기
    max_safe_time = -1
    best_r, best_c = -1, -1
    
    # 행, 열을 위에서부터, 왼쪽에서부터 순회하므로 
    # 조건 만족 시 자동으로 가장 상단-좌측 좌표가 최적해가 됨
    for r in range(rows):
        for c in range(cols):
            if final_mins[r][c] > max_safe_time:
                max_safe_time = final_mins[r][c]
                best_r, best_c = r, c
                
    return [best_r, best_c]