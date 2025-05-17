
answer = 0

def solution(n, q, ans):
    m = len(q)
    
    # 1부터 n 까지 중에서 5개 조합하는 함수
    # 조합이 완료되면, 조건을 만족하는지 체크한다.
    
    def check(code): # 조건 체크 함수
        for i in range(m):  # m 개의 코드를 모두 비교
            cnt = 0
            for j in range(5):
                if q[i][j] in code: # 받아온 코드에 숫자가 들어있다면 카운트
                    cnt += 1
            # 이 시점에서 한개의 코드를 비교했음
            if cnt != ans[i]:
                break   # 해당 코드가 시스템 응답과 일치하지 않음
        else:   # forelse문 - break 없이 다 했구나!
            return True # 가능한 코드임
        return False
    
    def f(n, arr, start):
        global answer
        if len(arr)==5:
            if check(arr):
                answer += 1
                return
            return
        for i in range(start,n+1):
            arr.append(i)
            f(n,arr,i+1)
            arr.pop()
    
    f(n, [], 1)
    
    return answer