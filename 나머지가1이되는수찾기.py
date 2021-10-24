def solution(n):
    n -= 1
    for i in range(2, n+1):
        if n % i == 0:
            answer = i
            break
    return answer

# 다른 사람 풀이
def solution(n):
    answer = min([x for x in range(1, n+1) if n % x == 1])
    return answer