def solution(phone_number):
    phone_number = list(phone_number)
    for i in range(len(phone_number)-5, -1, -1):
        phone_number[i] = '*'
    answer = ''.join(phone_number)
    return answer

print(solution("01033334444"))