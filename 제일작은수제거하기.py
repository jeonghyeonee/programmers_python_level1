def solution(arr):
    arr.remove(min(arr))
    answer = arr
    if len(arr) < 1:
        answer.append(-1)
    return answer
