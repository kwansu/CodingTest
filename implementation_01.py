'''
<상하좌우>
A는 N X N 크기의 정사각형 공간 위에 서 있다. 이 공간은 1 x 1 크기의 정사각형으로 
나누어져 있다. 가장 왼쪽 위 좌표는 (1, 1)이며, 가장 오른쪽 아래 좌표는 (N, N)에 해당한다.
A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 (1, 1)이다.
A는 이동 계획서에 따라 이동한다. 계획서에는 L, R, U, D 중 하나의 문자가 반복적으로 적혀 있다.
L : 왼쪽으로 이동
R : 오른쪽으로 이동
U : 위로 이동
D : 밑으로 이동
이 때, A가 N X N 크기의 정사각형 공간을 벗어나는 움직임은 무시된다.
계획서가 주어졌을 때, A가 최종적으로 도착할 지점의 좌표를 출력하라.
 -첫째 줄에 공간의 크기를 나타내는 N이 주어진다. (1 <= N <= 100)
 -둘째 줄에 A가 이동할 계획서 내용이 주어진다. (1 <= 이동 횟수 <= 100)
'''

N = int(input())
orders = input().split()
pos = [1, 1]

def move(pos, dir):
    pos[0] += dir[0]
    pos[0] = max(1, min(N, pos[0]))
    pos[1] += dir[1]
    pos[1] = max(1, min(N, pos[1]))

for c in orders:
    if c == 'L':
        move(pos, (-1, 0))
    elif c == 'R':
        move(pos, (1, 0))
    elif c == 'U':
        move(pos, (0, -1))
    elif c == 'D':
        move(pos, (0, 1))
    else:
        raise Exception

print(f"최종 위치 : {pos[0]} {pos[1]}")