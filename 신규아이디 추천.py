 # 어떻게 풀어야하지...
 
def solution(new_id):
    l = len(new_id)
    answer = ''
    new_id = string.lower(new_id)
    if l>=16:
        answer = new_id[:14]
        
    return answer