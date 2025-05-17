def solution(distance, rocks, n):
    answer = 0
    # 바위를 정렬
    rocks.sort()
    rocks.append(distance)  # 마지막 지점 추가
    
    # 이론상 가장 안좋은 값은?
    left = 1
    # 이론상 최고의 값은?
    right = distance    # 나누기 0 방지, 나머지 감안하여 +1
    
    while left <= right:
        cnt = 0 # 제거한 돌 카운트
        mid = (left+right)//2   # 이 거리가 가능한가?
        # 두 돌 사이의 거리가 mid 보다 작으면 안된다. 돌을 제거한다.
        # 돌을 하나 제거했는데도 mid보다 작으면, mid 이상이 될 때까지 제거하여야 한다.
        prev = 0
        for rock in rocks:
            if rock - prev < mid:
                cnt += 1
            else:
                prev = rock
            if cnt > n:
                right = mid-1
                break
        else:
            left = mid+1
            answer = mid
                
    
    return answer