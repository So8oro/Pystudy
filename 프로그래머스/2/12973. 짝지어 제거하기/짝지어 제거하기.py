def solution(s):
    answer = -1
    stack = []
    
    for char in s:
        if stack and char == stack[-1]:
                stack.pop()
        else: stack.append(char)

    return 0 if stack else 1