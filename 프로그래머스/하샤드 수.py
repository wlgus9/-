def solution(x):
    answer = True
    
    n = x
    sum = 0
    
    while True:
        sum = sum + (n % 10)
        n = int(n / 10)
        
        if n<=0:
            break

    if x % sum == 0:
        return answer
    else:
        answer = False
        return answer