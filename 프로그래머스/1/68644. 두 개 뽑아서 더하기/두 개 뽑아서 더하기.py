from itertools import combinations

def solution(numbers):
    answer = [a+b for a,b in combinations(numbers,2)]
    return sorted(list(set(answer)))