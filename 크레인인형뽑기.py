def solution(board, moves):
    answer = 0
    list = []
    
    for i in moves:
        for j in board:
            if j[i-1] != 0:
                list.append(j[i-1])
                
                if len(list) > 1:
                    if list[-2] == list[-1]:
                        del list[-2]
                        del list[-1]
                        answer += 2
                j[i-1] = 0
                break
    return answer