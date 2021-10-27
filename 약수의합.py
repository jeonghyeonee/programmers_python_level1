def solution(n):
    divisor = []
    for i in range(1, n+1):
        if n % i == 0:
            divisor.append(i)
    answer = sum(divisor)
    return answer
# another answer
def solution(n):
    return sum([i for i in range(1, n+1) if n%i == 0])