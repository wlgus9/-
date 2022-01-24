import sys
sys.stdin = open('섹션 2/2. K번째 수/in1.txt', 'r')

t = int(input())

for i in range(t):
    n, s, e, k = map(int, input().split())
    num = list(map(int, input().split()))
    
    num_split = num[s-1:e]
    num_split.sort()
    
    print(f'#{i+1} {num_split[k-1]}')