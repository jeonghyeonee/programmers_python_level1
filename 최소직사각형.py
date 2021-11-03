def solution(sizes):
    w = []
    h = []
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            w.append(sizes[i][0])
            h.append(sizes[i][1])
        else:
            h.append(sizes[i][0])
            w.append(sizes[i][1])

    return max(w) * max(h)

# 다른 사람 풀이
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

# w, h 중 큰 값을 모음
# 그 중 큰 값, w, h 중 작은 값을 모아서 그 중 큰 값을 곱함
