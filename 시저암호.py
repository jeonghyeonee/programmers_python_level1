def solution(s, n):
    answer = ''
    for i in s:
        i = ord(i)
        
        if i == 32:
            answer += " "
            continue

        if 65<=i<=90:
            idx = i + n
            if idx>90:
                idx -= 26
        
        else:
            idx = i + n
            if idx > 122:
                idx -= 26

        char = chr(idx)
        answer+= char
    return answer

print(solution("a B z", 4))