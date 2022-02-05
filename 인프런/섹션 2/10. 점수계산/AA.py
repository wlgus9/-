import sys
sys.stdin=open('섹션 2/10. 점수계산/in1.txt', 'r')
n = int(input())
a = list(map(int, input().split()))

cnt = 0
score = 0

for i in range(n):
    if a[i] == 1:
        cnt += 1
        score += cnt
    else:
        cnt = 0
        
print(score)        