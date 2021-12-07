# 파이썬에서는 "true"가 아니라 True로 입력해주어야 함!

def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer