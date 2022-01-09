def solution(dartResult):
    # 10은 예외처리 > 안 하면 1, 0 으로 나누어짐 
    arr = dartResult.replace("10", "A")
    stack = []
    
    for i in arr:
        
        if i.isdigit() or i == "A":
            if i == "A":
                stack.append(10)
            else:
                stack.append(int(i))
        
        elif i == 'S':
            n = stack.pop()
            stack.append(n**1)
        
        elif i == 'D':
            n = stack.pop()
            stack.append(n**2)
        
        elif i == 'T':
            n = stack.pop()
            stack.append(n**3)
        
        elif i == "#":
            stack[-1] *= -1
        
        elif i == "*":
            n = stack.pop()
            if len(stack): 
                stack[-1] *= 2
            stack.append(2*n)
    return sum(stack)