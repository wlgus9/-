import sys
sys.stdin=open("섹션 2/7. 소수(에라토스테네스 체)/in1.txt", "r")
n = int(input())

cnt = 0
check = [0] * (n+1)
for i in range(2, n+1):
    if check[i] == 0:
        cnt+=1
        for j in range(i, n+1, i):
            check[j] = 1
            
print(cnt)          