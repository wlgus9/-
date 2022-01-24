import sys
sys.stdin=open("섹션 2/6. 자릿수의 합/in1.txt", "r")
n = int(input())
num_list = list(map(int, input().split()))


def digit_sum(x):
    sum = 0
    while True:
        sum = sum + x%10
        x = x//10   
        if x <= 0:
            break
    return sum

res = 0
max = 0
num = 0
for i in num_list:
    res = digit_sum(i)
    if res > max:
        max = res
        num = i

print(num)