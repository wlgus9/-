import sys
sys.stdin=open("자릿수의 합/in1.txt", "r")
n = int(input())
num_list = list(map(int, input().split()))

# n = 15
# num_list = [770, 93, 883, 659, 641, 446, 354, 227, 338, 178, 510, 357, 560, 362, 884]

def digit_sum(x):
    sum = 0
    while x>0:
        sum += x%10
        x /= 10
    return sum

result = 0
max = 0
for i in num_list:
    total_sum = digit_sum(i)
    if total_sum > max:
        max = total_sum
        result = i
print(result)        