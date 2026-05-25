def solution(s):
    answer = ''
    cnt = 0
    for a in s:
        if a==' ':
            answer += ' '
            cnt = 0
            continue
        if cnt%2:
            answer += a.lower()
        else:
            answer += a.upper()
        cnt += 1
    return answer