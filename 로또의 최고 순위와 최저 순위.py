def solution(lottos, win_nums):
    answer = []
    for i in lottos:
        if i in win_nums:
            win_nums.remove(i)
    
    l = len(win_nums)
    z = lottos.count(0)
    rank = {0:1, 1:2, 2:3, 3:4, 4:5, 5:6, 6:6}
    for r in rank:
        if l == r:
            answer.append(rank[r])
            if l <= z:
                answer.append(rank[r-l])
            else:
                answer.append(rank[r-z])
    answer.sort()
    return answer

print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))