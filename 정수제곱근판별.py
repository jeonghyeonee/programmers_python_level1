import math

def solution(n):
    answer = -1
    s = math.sqrt(n)
    if n%s == 0:
        answer = (s+1)**2
    return answer