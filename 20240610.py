#문자열 내 p/y 개수
def solution(s):
    answer = True

    p_cnt = 0
    y_cnt = 0
    for i in s:
        if i == "p" or i == "P":
            p_cnt += 1
        elif i == "y" or i == "Y":
            y_cnt += 1
        else:
            pass
    
    if p_cnt != y_cnt:
        answer = False

    return answer

def other_solution(s):
    return s.lower().count('p') == s.lower().count('y') 

print(other_solution("pPoooyY"))
print(other_solution("Pyy"))

# 문자열을 정수로 바꾸기
def solution(s):
    answer = int(s)
    return answer

# 약수의 합
def solution(n):
    list = []
    for i in range(1, n+1):
        if n%i == 0:
            list.append(i)
    return sum(list)

def soltuion (n):
    answer = 0
    for i in range(1, n//2+1):
        if n%i == 0:
            answer += i
    answer += n
    return answer

def othersolution(n):
    return n + sum([i for i in range(1, (n//2) + 1) if n%i == 0])

# 자릿수 더하기
def solution(n):
    answer = 0
    n = str(n)
    
    for i in range(len(n)):
        answer += int(n[i])

    return answer
# 재귀로 푸는 자릿수 더하기
def othersolution(n):
    if n < 10:
        return n
    return n%10 + othersolution(n//10)

# 자연수 뒤집어 배열로 만들기
def solution(n):
    n = str(n)
    answer = list(n[::-1])
    answer = [int(i) for i in answer]
    return answer

def othersolution(n):
    return list(map(int, reversed(str(n))))

# 정수 내림차순으로 배치하기
def solution(n):
    n = list(str(n))
    n = int((''.join(reversed(sorted(n)))))
    return n

# 정수 제곱근 판별
import math

def solution(n):
    answer = 0
    if math.sqrt(n) == int(math.sqrt(n)):
        answer = math.pow((math.sqrt(n) + 1), 2)
    else:
        answer = -1
    return answer

def othersolution(n):
    sqrt = n ** (1/2)

    if sqrt%1 == 0:
        return (sqrt + 1) ** 2
    return -1

# 짝수와 홀수
def solution(num):
    if num%2 == 0:
        return "Even"
    else:
        return "Odd"