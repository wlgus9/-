import sys
sys.stdin=open("뒤집은 소수/in1.txt", "r")
n = int(input())
a = list(map(int, input().split()))

def reverse(x):
    res = 0
    while x>0:
        t = x%10
        res = res*10+t
        x = x//10    
    return res   

def isPrime(x):
    if x==1:
        return False
    for i in range(2, x):
        if x%i==0:
            return False
    return True

for i in a:
    result = reverse(i)
    if isPrime(result):
        print(result, end=' ')
