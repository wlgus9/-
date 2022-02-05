import sys
sys.stdin=open("섹션 2/9. 주사위 게임/in1.txt", "r")
n = int(input())

max=0
for i in range(n):
    money = 0
    
    dice = list(map(int, input().split()))
    dice.sort()
    a, b, c = 0, 1, 2
    
    if (dice[a] == dice[b]) & (dice[b] == dice[c]):
        money = 10000 + dice[a]*1000
    elif (dice[a] == dice[b]) | (dice[b] == dice[c]):
        money = 1000 + dice[b]*100
    else:
        money = dice[c]*100

    if money > max:
        max = money
        
print(max)        