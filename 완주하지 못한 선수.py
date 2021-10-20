def solution(participant, completion):
    # for i in completion:
    #     if i in participant:
    #         participant.remove(i)
    # for i in part이ipant:
    #     answer = i
    # return answer

    completion.sort()
    participant.sort()
    
    for idx, p in enumerate(participant):
        if p != completion[idx]:
            return p

# 효율성 통과 못 한 이유
# remove, if -> O(n^2)

# 다른 사람 풀이
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p,c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop()

# 다른 사람 풀이
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]