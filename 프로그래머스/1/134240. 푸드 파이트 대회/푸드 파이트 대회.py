def solution(food):
    answer = ''
    for idx, f in enumerate(food):
        answer += str(idx)*(f//2)
    return answer+'0'+answer[::-1]