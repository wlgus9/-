import sys
sys.stdin = open('섹션 3/4. 두 리스트 합치기/in1.txt', 'r')

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.extend(b)
a.sort()

c = ' '.join(str(_) for _ in a)
print(c)