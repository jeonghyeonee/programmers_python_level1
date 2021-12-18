# 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# N = 전체 스테이지의 개수, stages = 현재 멈춰있는 스테이지의 번호
# 실패율이 높은 스테이지부터 내림차순으로 스테이지 번호 정렬 return
# dictionary 쓰면 풀 수 있을 것 같은데...

def solution(N, stages):
    answer = {}
    l = len(stages)
    for i in range(1, N+1):
        if l != 0:
            cnt = stages.count(i)
            answer[i] = cnt / l
            l -= cnt
        else:
            answer[i] = 0
    result = sorted(answer, key=lambda x : answer[x], reverse=True)
    return result