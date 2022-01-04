def solution(answers):
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    
    s =[0, 0, 0]
    l = len(answers)
    for i in range(l):
        if answers[i] == p1[i%5]:
            s[0] += 1
        if answers[i] == p2[i%8]:
            s[1] += 1
        if answers[i] == p3[i%10]:
            s[2] += 1
    
    m = max(s)
    answer = []
    
    for i in range(len(s)):
        if s[i] == m:
            answer.append(i+1)

    return answer