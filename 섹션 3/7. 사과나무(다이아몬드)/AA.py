import sys
sys.stdin = open('섹션 3/7. 사과나무(다이아몬드)/in1.txt', 'r')

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

sum = 0
s = e = n//2
for i in range(n):
    for j in range(s, e+1):
        sum += a[i][j]
    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
            
print(sum)            