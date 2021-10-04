'''
어떤한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다.
단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.
    1. N에서 1을 뺀다.
    2. N을 K로 나눈다.

N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야하는 최소 횟수를 구하여라.

    -첫째 줄에 N(2 <= N <= 100000)과 K(2 <= K <= 100000)가 공백으로 구분되며 각각 자연수로
    주어진다. 이때 입력으로 주어지는 N은 항상 K보다 크거나 같다.
    -첫째 줄에 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야하는 횟수의 최솟값을 출력한다.
'''


N, K = map(int, input().split())

count = 0
while N != 0:
    share, remainder = divmod(N, K)
    if remainder == 0:
        N = share
        count += 1
    else:
        N -= remainder
        count += remainder

print(f"최소 횟수 : {count - 1}")