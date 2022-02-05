def solution(s):
    l = list()
    for i in range(len(s)):
        l.append(ord(s[i]))
    
    l.sort(reverse=True)
    
    for i in range(len(l)):
        l[i] = chr(l[i])
    
    return ''.join(l)