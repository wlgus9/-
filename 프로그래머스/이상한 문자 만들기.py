def solution(s):
    answer = []
    word = s.split(' ')
    for i in range(len(word)):
        for j in range(len(word[i])):
            if j%2==0:
                answer.append(word[i][j].upper())
            else:
                answer.append(word[i][j].lower())
        answer.append(' ')
    answer.pop(-1)
    answer = ''.join(str(_) for _ in answer)
    return answer