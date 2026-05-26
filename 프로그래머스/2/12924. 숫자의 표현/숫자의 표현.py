def solution(n):
    answer = 1  # 1개의 자연수로 표현 가능
    nn = n*2
    
    # i개의 자연수로 표현 가능한지 확인할 것
    # i의 이론상 최댓값은? 1부터i의합이 n을 초과하면 불가능함
    # 따라서, int((2*n)**(1/2))
    maxi = int((2*n)**(1/2))
    print(maxi)
    
    # i가 홀수인 경우
    # i로 나누어떨어져야하고, 1부터i의합 = 1+i//2*i 이상이어야 함
    for i in range(3,maxi+1,2):
        if n%i==0 and 1+i//2*i <= n: answer += 1

    # i가 짝수인 경우
    # n*2가 i로 나누어떨어져야하고, n은 i로 나누어떨어지지않고, (1+i)*i 이상이어야 함
    for i in range(2,maxi+1,2):
        if nn%i==0 and n%i!=0 and (1+i)*i <= nn: answer += 1
    
    return answer

# def solution(num):
#     return len([i  for i in range(1,num+1,2) if num % i is 0])
