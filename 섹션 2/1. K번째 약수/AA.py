import sys
sys.stdin = open('섹션 2/1. K번째 약수/in1.txt', 'r')

n, k = map(int, input().split())
cnt = list()

for i in range(1, n+1):
    if n%i==0:
        cnt.append(i)     
            
if len(cnt) >= k:
    print(cnt[k-1])
elif len(cnt) < k:
    print(-1)