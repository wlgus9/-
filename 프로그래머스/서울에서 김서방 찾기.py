def solution(seoul):
    answer = ''
    a = 0
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            a = i
            break
    return f'김서방은 {a}에 있다'