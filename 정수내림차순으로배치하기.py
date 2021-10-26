def solution(n):
    n = sorted(str(n), reverse=True)
    n = ''.join(n)
    answer = int(n)
    return answer