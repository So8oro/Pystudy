N = int(input())+1  # 0은 0번째 감소하는 수여서 보정

numbers = (9,8,7,6,5,4,3,2,1,0)
decreasing_number = []
number_arr = []

# 9876543210 중에서 n개를 조합하여 decreasing_number에 추가하는 함수
# 이 경우, n자리의 모든 감소하는 수가 생성되며, 조합 선택 순서에 따라 내림차순으로 생성됨
def f(n, start):
    if len(number_arr) == n:
        decreasing_number.append(number_arr[:])
        return
    else:
        for i in range(start,10):
            number_arr.append(numbers[i])
            f(n,i+1)
            number_arr.pop()

# 내림차순으로 모든 감소하는 수를 생성
for i in range(10,0,-1):
    f(i,0)

if len(decreasing_number) < N:
    print(-1)
else:
    print(''.join(map(str,decreasing_number[-N])))