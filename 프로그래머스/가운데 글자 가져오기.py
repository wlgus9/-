def solution(s):
    answer = ''
    l = len(s)//2
    
    if len(s)%2==0:
        answer = s[l-1:l+1]
    else:
        answer = s[l]
    
    return answer