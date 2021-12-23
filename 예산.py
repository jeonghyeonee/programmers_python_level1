# 뭐가 문제인거지??
# 오늘도 해결 못했다!
# 최대한 많은 부서! -> 정렬 추가!

def solution(d, budget):
    d.sort()
    answer = 0
    for i in d:
        budget -= i
        if budget < 0:
            break
        answer += 1
    return answer