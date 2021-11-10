def solution(x):
    answer = False
    x = str(x)
    n = 0
    for i in x:
        n += int(i)
    if int(x) % n == 0:
        answer = True
    return answer