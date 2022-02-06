def solution(price, money, count):
    sum = price
    
    for i in range(2, count+1):
        sum += price*i
        
    if (money-sum) > 0:
        return 0
    else:
        return sum-money