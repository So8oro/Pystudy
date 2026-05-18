def solution(s):
    
    answer = 0
    
    for a in s:
        if a=='(':
            answer += 1
        else:
            answer -= 1
        if answer<0: return False
    
    return not answer