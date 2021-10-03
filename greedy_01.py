'''
당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원, 100원, 
50원 10원짜리 동전이 무한히 존재한다고 가정한다. 손님이에게 거슬러 줘야 할 돈이 N원일 때 
거슬러 줘야 할 동전의 최소 개수를 구하라. 단, 거슬러 줘야 할 돈 N은 항상 10의 배숭이다.
'''

N = 1370

coins = [500, 100, 50, 10]
result = {}

for coin_size in coins:
    count, N = divmod(N, coin_size)
    result[coin_size] = count

assert(N == 0)

for key, value in result.items():
    print(f"{key}원의 개수 : {value}개")

print(f"총 동전의 개수 : {sum(result.values())}개")