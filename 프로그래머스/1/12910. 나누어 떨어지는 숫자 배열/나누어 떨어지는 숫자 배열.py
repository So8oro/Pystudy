def solution(arr, divisor):
    answer = []
    for num in arr:
        if not num%divisor:
            answer.append(num)
    if answer:
        answer.sort()
    else: answer = [-1]
    return answer