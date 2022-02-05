def solution(num):
    x = num
    sum = 0
    
    while True:
        if x%2==0:
            x /= 2
            sum += 1
        elif x == 1:
            return 0
        else:
            x = x*3+1
            sum += 1
        if sum >= 500:
            return -1
        elif x == 1:
            break
    
    return sum