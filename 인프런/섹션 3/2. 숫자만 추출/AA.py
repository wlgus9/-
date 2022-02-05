import sys
sys.stdin = open('섹션 3/2. 숫자만 추출/in1.txt', 'r')

n = input()
num = 0
for i in n:
    if i.isdecimal():
        num = num*10 + int(i)
print(num)

cnt = 0
for i in range(1, num+1):
    if num % i == 0:
        cnt+=1
                  
print(cnt)