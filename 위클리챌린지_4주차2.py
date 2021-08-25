def solution(table, languages, preference):
    score = []
    # table 2차원 리스트로 변경
    # table 정렬하기
    # why? 동일 점수일 경우 더 앞쪽의 것을 가져오기 위함
    new_table = sorted([list(i.split()) for i in table], key=lambda  x:x[0])
    type = {i:new_table[i][0] for i in range(len(new_table))}

    for i in range(len(type)):
        s = 0
        for l, p in zip(languages, preference):
            if l in new_table[i]:
                s += (6-new_table[i].index(l))*p
        score.append(s)

    return type[score.index(max(score))]

table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]

print(solution(table, languages, preference))
print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"], [7, 5]))
