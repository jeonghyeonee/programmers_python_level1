# 뭐가 문제인거지??

def solution(d, budget):
    answer = 0
    for i in d:
        budget -= i
        if budget < 0:
            break
        answer += 1
    return answer