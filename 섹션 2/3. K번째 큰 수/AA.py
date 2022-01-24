import sys
sys.stdin = open('섹션 2/3. K번째 큰 수/in1.txt', 'r')

n, k = map(int, input().split())
card = list(map(int, input().split()))

sum = list()

for i in range(n):
    for j in range(i):
        for h in range(j):
            sum.append(card[i] + card[j] + card[h])
            
sum = set(sum)     
sum = list(sum)       
sum.sort(reverse=True)
print(sum[k-1])
        