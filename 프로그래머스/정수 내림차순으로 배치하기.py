def solution(n):
    answer = 0
    s = list()
    while n > 0:
        s.append(n%10)
        n = n//10
    s.sort(reverse=True)
    answer = ''.join(str(_) for _ in s)  
    return int(answer)