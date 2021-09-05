def solution(v):
    
    x1 = v[0][0]
    y1 = v[0][1]
    x2 = v[1][0]
    y2 = v[1][1]
    x3 = v[2][0]
    y3 = v[2][1]
    result = []

    
    if (x1 == y1 and x2 == y2) or (x1 == y1 and x3 == y3) or (x2 == y2 and x3 == y3):
        for i in v:
            if i[0] != i[1]:
                result += [i[1], i[0]]
                return result
            else:
                continue
    if x1 == x2:
        result.append(x3)
    elif x1 == x3:
        result.append(x2)
    elif x2 == x3:
        result.append(x1)

    if y1 == y2:
        result.append(y3)
    elif y1 == y3:
        result.append(y2)
    elif y2 == y3:
        result.append(y3)

    return result