import sys
sys.stdin=open("섹션 2/5. 정다면체/in1.txt", "r")

n, m=map(int, input().split())

sum = list()
cnt = [0] * (n+m+1)
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] = cnt[i+j] + 1

max=0
for i in range(len(cnt)):
    if cnt[i] > max:
        max = cnt[i]
        
for i in range(len(cnt)):
    if cnt[i] == max:
        print(i, end=' ')