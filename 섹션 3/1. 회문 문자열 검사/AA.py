import sys
sys.stdin = open('섹션 3/1. 회문 문자열 검사/in1.txt', 'r')

n = int(input())

for i in range(1, n+1):
    word = input()  
    word = word.upper()
    for j in range(len(word)//2):
        if word[j] != word[-1-j]:
            print(f'#{i} NO')
            break
    else:
        print(f'#{i} YES')