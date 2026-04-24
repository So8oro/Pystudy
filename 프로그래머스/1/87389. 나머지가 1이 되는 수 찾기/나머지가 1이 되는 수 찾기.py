def solution(n):
    for x in range(2, int(n**(0.5)+1)):
        if n%x==1: return x
    return n-1