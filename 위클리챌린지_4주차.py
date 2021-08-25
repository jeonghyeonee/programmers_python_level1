def solution(table, languages, preference):
    # 문제점 동일 최댓값에 대한 해결을 하지 못함 -> 46점
    for i in range(len(table)):
        table[i] = list(table[i].split(" "))

    score = [0 for _ in range(5)]

    for i in range(5):
        for j in range(len(languages)):
            if languages[j] in table[i]:
                score[i] += preference[j]*(table[i].index(languages[j]))
            else:
                continue

    idx = score.index(max(score))
    answer = table[idx+1][0]
    return answer


table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]

print(solution(table, languages, preference))
print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"], [7, 5]))
