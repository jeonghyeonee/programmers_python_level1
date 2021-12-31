# https://jokerldg.github.io/algorithm/2021/04/23/secret-map.html

def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        value = str(bin(i|j)[2:])
        value = value.zfill(n)
        value = value.replace('1', '#')
        value = value.replace('0', ' ')
        answer.append(value)
    return answer