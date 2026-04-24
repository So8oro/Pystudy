def solution(s):
    answer = 1
    
    for x in s:
        if x=='P' or x=='p':
            answer += 1
        elif x=='Y' or x=='y':
            answer -= 1

    return (answer==True)