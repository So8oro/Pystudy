def solution(s):
    answer = ''
    isFirst = True
    for l in s:
        if l == ' ':
            isFirst = True
            answer += ' '
            continue
        if isFirst:
            answer += l.upper()
            isFirst = False
        else: answer += l.lower()
    
    return answer