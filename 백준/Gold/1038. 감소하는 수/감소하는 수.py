N = int(input())

que = [0,1,2,3,4,5,6,7,8,9]     # 감소하는 수가 들어갈 큐. 오름차순이 항상 유지되는 구조로 코드 작성.
cnt = -1    # 몇 번째 감소하는 수인지 카운트

while que:
    num = que.pop(0)    # 큐에 있는 가장 작은 감소하는 수 pop
    cnt += 1
    if cnt == N:
        print(num)      # N번째 감소하는 수면 출력하고 종료
        break
    else:
        for i in range(10):     # i는 0부터 9까지의 수
            if i < num%10:      # 감소하는 수의 1의 자리보다 더 작은 i가 있다면,
                que.append(num*10+i)        # 감소하는 수 뒤에 붙인다! 그럼 이것 역시 감소하는 수이다. 이건 찾은 것 중 가장 큰 수이다.
else:       # break문이 실행되지 않았다면, N번째 감소하는 수가 존재하지 않는 것
    print(-1)