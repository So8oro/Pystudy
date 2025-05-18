from collections import Counter

def solution(participant, completion):
    p = Counter(participant)
    c = Counter(completion)
    result = p - c  # Counter의 뺄셈은 개수 차를 유지
    return list(result.keys())[0]