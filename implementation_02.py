'''
정수 Ndl 입력되며 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 
포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.
 - 첫째 줄에 정수 N이 입력된다.(0 <= N <= 23)
'''

N = int(input())


m_s_count = 60*60 - 5*9*5*9
h_3_count = 0
for h in (3, 13, 23):
    if N < h:
        break
    h_3_count += 1

count = h_3_count * 60*60 + (N - h_3_count + 1) * m_s_count

print(count)
