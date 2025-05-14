N, K = map(int, input().split())

V = [0] * (N + 1)  # 부피
C = [0] * (N + 1)  # 가치

for i in range(1, N + 1):
    V[i], C[i] = map(int, input().split())

# dp[i][j] : i물건까지 고려해 부피 j를 채웠을 때의 최대가치
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):

        # 배낭보다 물건이 큰 경우
        if V[i] > j:
            dp[i][j] = dp[i - 1][j]  # i물건없이 j를 채운경우

        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - V[i]] + C[i])

        '''
        새로운 물건을 추가할 때 가치가 높아지는지를 보려면 두 경우를 체크한다.
        1. 그냥 안 추가하는 경우. dp[i - 1][j]
        2. 새로운 물건을 추가. 단 가방 안에 충분한 공간이 없을 수 있으니, 우선 가방을
            적당히 비워준다. 딱 새로운 물건이 들어갈 수 있을 정도로 + 해당 부피에서 최대 가치가
            유지되도록. dp[i - 1][j - V[i]]
            그리고 새로운 물건을 추가한다. + C[i]

        이렇게 부피를 트래킹 할 수 있어야하므로 2차원 배열이 필요한 것.
        '''

print(dp[N][K])