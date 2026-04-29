def solution(n):
    answer = ''
    for i in range(n):
        if answer[-1:]!="수":
            answer += "수"
        else: answer += "박"
    return answer