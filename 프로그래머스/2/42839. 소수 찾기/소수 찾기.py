from collections import Counter

def solution(numbers):
    answer = 0
    # 일단 9999999 까지 모든 소수를 다 찾아두자
    primes = [True] * 10000000
    primes[0] = primes[1] = False
    for i in range(2, int(10000000**0.5)):
        if primes[i]:
            for j in range(i*i, 10000000, i):
                primes[j] = False
    # 숫자 조각이 몇개씩 있나 세어두자
    numbercount = Counter(numbers)
    for i in range(2,10000000):
        if primes[i]:
            primecount = Counter(str(i))
            for item, count in primecount.items():
                if numbercount[item] < count: break
            else: answer += 1
    return answer