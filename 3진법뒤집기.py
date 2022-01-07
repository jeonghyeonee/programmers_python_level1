def solution(n):
    answer = ''
    #3진법 만들기, 뒤집기 
    while n > 0:
        n, mod = divmod(n, 3)
        answer += str(mod)

    #10진법 만들기
    answer = int(answer, 3)
    return answer

print(solution(45))