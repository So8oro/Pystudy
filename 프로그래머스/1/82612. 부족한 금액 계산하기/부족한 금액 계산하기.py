def solution(price, money, count):
    tot = price*(1+count)*count/2
    if tot<money: return 0
    return tot-money