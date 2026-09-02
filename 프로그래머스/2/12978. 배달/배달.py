import heapq

def solution(N, road, K):
    answer = 0
    
    cost = [K+1 for _ in range(N+1)]    # 각 마을까지 걸리는 시간을 저장. 최대로 초기화
    cost[1] = 0
    
    # heapq는 첫 번째 원소 기준으로 정렬하므로 [시간, 마을] 순서
    pq = [[0, 1]]    # [시간, 마을]
    
    while pq:
        t, n = heapq.heappop(pq)
        if t > cost[n]: continue
            
        # 현재 마을에서 연결된 모든 마을을 찾자
        for town1, town2, time in road:
            
            # Case 1: 출발지가 town1인 경우
            if town1 == n:
                if cost[town2] > cost[town1] + time:
                    cost[town2] = cost[town1] + time
                    heapq.heappush(pq, [cost[town2], town2]) 
                    
            # Case 2: 출발지가 town2인 경우
            elif town2 == n:
                if cost[town1] > cost[town2] + time:
                    cost[town1] = cost[town2] + time
                    heapq.heappush(pq, [cost[town1], town1])

    return sum(1 for c in cost if c <= K)
