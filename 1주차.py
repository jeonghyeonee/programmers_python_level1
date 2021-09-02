def solution(price, money, count):
    total = 0
    for i in range(1, count+1):
        p = price * i
        total += p
    if money >= total:
        answer = 0
    else:
        answer = total - money
    return answer

print(solution(3, 20, 4))