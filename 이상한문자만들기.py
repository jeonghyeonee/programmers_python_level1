def solution(s):
    n = s.split(' ')
    answer = ''
    for i in range(len(n)):
        for j in range(len(n[i])):
            if j%2 == 0:
                answer += n[i][j].upper()
            else:
                answer += n[i][j].lower()
        if i == len(n):
            break
        answer += ' '
    return answer

print(solution("try hello world"))