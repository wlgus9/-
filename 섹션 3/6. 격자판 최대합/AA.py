import sys
sys.stdin = open('섹션 3/6. 격자판 최대합/in1.txt', 'r')

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
row = 0
col = 0
max = 0

for i in range(n):
    for j in range(n):
        row = row + a[i][j]
        col = col + a[j][i]
        
        if row > max:
            max = row
        if col > max:
            max = col       
    row = 0
    col = 0
    
dia1, dia2 = 0, 0
r = 0
c = n-1
for i in range(n):
    dia1 = dia1 + a[i][i]
    dia2 = a[c-i][r+i]
    if dia1 > max:
        max = dia1
    if dia2 > max:
        max = dia2

print(max)