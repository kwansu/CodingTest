'''
당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원, 100원, 
50원 10원짜리 동전이 무한히 존재한다고 가정한다. 손님이에게 거슬러 줘야 할 돈이 N원일 때 
거슬러 줘야 할 동전의 최소 개수를 구하라. 단, 거슬러 줘야 할 돈 N은 항상 10의 배숭이다.
'''

N = 1370

count_500, remainder = divmod(N, 500)
count_100, remainder = divmod(remainder, 100)
count_50, remainder = divmod(remainder, 50)
count_10, remainder = divmod(remainder, 10)

assert(remainder == 0)

print(f"500원 개수:{count_500}개, 100원 개수:{count_100}개, 50원 개수:{count_50}개, 10원 개수:{count_10}개")
