import sys
read = sys.stdin.readline

n,k = map(int, read().split())
coin = []
for i in range(n):
    coin.append(int(read()))

coin.sort(reverse=True)

_sum = 0
inx = 0
count = 0
while _sum < k:
    if inx > len(coin):
        break

    if _sum + coin[inx] <= k:
        _sum += coin[inx]
        count += 1
    else:
        inx += 1

print(count)
