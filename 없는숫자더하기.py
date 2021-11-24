def solution(numbers):
    answer = [i for i in range(10)]
    for i in numbers:
        answer.remove(i)
    return sum(answer)

# 다른사람의 풀이

def solution(numbers):
    return 45 - sum(numbers)