def solution(a, b):
    if a==b: return a
    return (a+b)*(abs(a-b)+1)/2