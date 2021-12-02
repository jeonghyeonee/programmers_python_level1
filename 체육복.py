# 단순하게 n에서 lost빼고 reserve 더하는 방식으로 풀어보려고 하지만, 안되는 케이스 존재
# https://jokerldg.github.io/algorithm/2021/04/03/gym-suit.html

def solution(n, lost, reserve):
    reserve_set = set(reserve)-set(lost) 
    lost_set = set(lost)-set(reserve) 
    
    for reserve_person in reserve_set: 
        if reserve_person-1 in lost_set: 
            lost_set.remove(reserve_person-1) 
        elif reserve_person+1 in lost_set: 
            lost_set.remove(reserve_person+1) 
    
    return n-len(lost_set)