def solution(arr):
    if not arr or len(arr)==1: return [-1]
    arr.remove(min(arr))
    return arr