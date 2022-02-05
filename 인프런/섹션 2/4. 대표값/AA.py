import sys
sys.stdin = open('섹션 2/4. 대표값/in1.txt', 'r')

n = int(input())
math = list(map(int, input().split()))

avg = sum(math)/len(math)
avg = round(avg)

min = 1000
score = 0
for idx, i in enumerate(math):
    tmp = abs(i-avg)
    if tmp < min:
        min = tmp
        score = i
        res = idx+1
    elif tmp == min:
        if i > score:
            score = i
            res = idx+1

print(avg, res)
