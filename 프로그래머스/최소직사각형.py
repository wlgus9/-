def solution(sizes):
    answer = 0
    width = list()
    height = list()
    max = 0
    min = 1001

    for i in range(len(sizes)):
        if sizes[i][0] > sizes[i][1]:
            width.append(sizes[i][0])
            height.append(sizes[i][1])
        else:
            width.append(sizes[i][1])
            height.append(sizes[i][0])

    w = width[0]
    h = height[0]    

    for i in range(1, len(width)):
        if w < width[i]:
            w = width[i]

        if h < height[i]:
            h = height[i]

    answer = w*h
    return answer