# lambda쓰면 풀릴 것 같은데, lambda로 못 품

def solution(strings, n):
    answer = []
    ns = []
    for i in strings:
        ns.append(i[n]+i)
    ns.sort()
    
    for i in ns:
        answer.append(i[1:])
                
    return answer

# 다른 사람의 풀이
def strange_sort(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    return sorted(strings, key=lambda x: x[n])

strings = ["sun", "bed", "car"] 
print(strange_sort(strings, 1))