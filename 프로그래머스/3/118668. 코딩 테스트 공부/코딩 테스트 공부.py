def solution(alp, cop, problems):
    
    target_alp = max(problem[0] for problem in problems)
    target_cop = max(problem[1] for problem in problems)

    alp = min(alp, target_alp)
    cop = min(cop, target_cop)

    INF = float('inf')

    # dp[a][c] = 알고력이 a이고 코딩력이 c인 상태에 도달하는 데 필요한 최소 시간
    dp = [[INF] * (target_cop + 1) for _ in range(target_alp + 1)]

    dp[alp][cop] = 0

    for a in range(alp, target_alp + 1):
        for c in range(cop, target_cop + 1):

            # 알고력 공부
            if a < target_alp:
                dp[a + 1][c] = min(dp[a + 1][c], dp[a][c] + 1)

            # 코딩력 공부
            if c < target_cop:
                dp[a][c + 1] = min(dp[a][c + 1], dp[a][c] + 1)

            # 문제 풀기
            for req_a, req_c, rwd_a, rwd_c, cost in problems:

                # 현재 능력치로 풀 수 있는지
                if a >= req_a and c >= req_c:

                    # 문제를 풀고 얻는 새로운 능력치
                    next_a = min(target_alp, a + rwd_a)
                    next_c = min(target_cop, c + rwd_c)

                    # 기존에 알고 있던 최소 시간 비교
                    dp[next_a][next_c] = min(dp[next_a][next_c], dp[a][c] + cost)

    return dp[target_alp][target_cop]