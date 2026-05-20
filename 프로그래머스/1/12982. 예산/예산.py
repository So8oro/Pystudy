def solution(d, budget):
    answer = 0
    money = 0
    for m in sorted(d):
        money += m
        if money <= budget:
            answer += 1
        else: return answer
    return answer