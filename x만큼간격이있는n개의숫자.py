def solution(x, n):
    answer = []
    s = 0
    for i in range(n):
        s += x
        answer.append(s)
    return answer
