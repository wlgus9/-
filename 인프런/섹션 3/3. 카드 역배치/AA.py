import sys
sys.stdin = open('섹션 3/3. 카드 역배치/in1.txt', 'r')

card = list(range(21)) #인덱스와 숫자를 일치시키기 위해 0부터 20까지의 값을 가지는 리스트 생성

for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2): #값을 변경하기 위해서 (끝 - 처음 + 1) // 2의 반복만 필요
                                #ex) 1부터 4를 역순으로 -> (1, 4), (2, 3) 이렇게 2번만 반복
        card[s+i], card[e-i] = card[e-i], card[s+i]

card.pop(0) #0번째 요소 삭제

for c in card:
    print(c, end=' ') #공백을 추가하여 출력

