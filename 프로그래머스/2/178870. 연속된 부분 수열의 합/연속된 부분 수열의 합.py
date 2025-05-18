# def solution(sequence, k):
#     answer = []
    
#     # 부분집합의 시작은 start, 끝은 end, 합은 sum
#     end = 0
#     sum = 0
#     length = len(sequence)
    
#     for start in range(len(sequence)):
#         while sum < k and end < len(sequence):
#             sum += sequence[end]  # 합 더하기
#             end += 1
#         if sum==k and end-start < length:
#             length = end-start    # 부분집합 최소 길이 갱신
#             answer = [start,end-1]
#         # 이제 합이 k이거나, 초과했음
#         sum -= sequence[start]
#     return answer

def solution(sequence, k):
    n = len(sequence)

    max_sum = 0
    end = 0
    interval = n

    for start in range(n):
        while max_sum < k and end < n:
            max_sum += sequence[end]
            end += 1
        if max_sum == k and end-1-start < interval:
            res = [start, end-1]
            interval = end-1-start
        max_sum -= sequence[start]

    return res