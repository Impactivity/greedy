import sys
read = sys.stdin.readline

n = int(read()) #도시의 개수
road_len = list(map(int, read().split()))
liter_price = list(map(int, read().split()))

_sum = road_len[0] * liter_price[0]
dist = 0
m = liter_price[0]

for i in range(1,n-1):
    if liter_price[i] < m :
        _sum += m*dist
        dist = road_len[i]
        m = liter_price[i]
    else :
        dist += road_len[i]

    if i == n-2:
        _sum += m * dist

print(_sum)
