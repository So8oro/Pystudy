def solution(s):
    answer = []
    save = dict()
    for idx, char in enumerate(s):
        if char in save:
            answer.append(idx-save[char])
            save[char] = idx
        else:
            save[char] = idx
            answer.append(-1)
    return answer