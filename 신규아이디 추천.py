# 문제를 차근차근 이해해보자 

def solution(new_id):
    l = len(new_id)
    answer = ''
    new_id = string.lower(new_id)
    if l>=16:
        answer = new_id[:14]
        
    return answer