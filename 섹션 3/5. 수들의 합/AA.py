import sys
sys.stdin = open('섹션 3/5. 수들의 합/in1.txt', 'r')

n, m = map(int, input().split())
a = list(map(int, input().split()))

sum = 0
cnt = 0
for i in range(n):
    for j in range(i, n):
        sum += a[j]
        if sum == m:
            cnt += 1
            break
    sum = 0

print(cnt)        