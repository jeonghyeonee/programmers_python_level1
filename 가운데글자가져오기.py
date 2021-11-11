def solution(s):
    l = len(s)
    idx = l//2 -1
    answer = ''
    if l%2 == 0:
        answer += s[idx]
        answer += s[idx+1]
    else:
        answer += s[idx+1]
    return answer