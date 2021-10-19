def solution(participant, completion):
    for i in completion:
        if i in participant:
            participant.remove(i)
    for i in participant:
        answer = i
    return answer