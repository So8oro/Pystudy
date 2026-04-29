def solution(arr):
    answer = []
    
    while(arr):
        pop = arr.pop()
        if answer == [] or pop != answer[-1]:
            answer.append(pop)
    
    answer.reverse()
    
    
    return answer