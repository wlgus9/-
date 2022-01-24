import sys
sys.stdin=open("섹션 2/8. 뒤집은 소수/in1.txt", "r")

n = int(input())
num = list(map(int, input().split()))

def reverse(x):
    rev = 0
    while x>0:
        t = x%10
        rev = rev * 10 + t
        x //= 10

    return rev

def isPrime(x):
    if x == 1:
        return False    
    for i in range(2, x):
        if x%i == 0:
            return False
    return True

for i in num:
    rev = reverse(i)
    if isPrime(rev):
        print(rev, end=' ')  