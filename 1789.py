#서로다른 n개 합 s가 주어질때 자연수 최댓값 n은 ?
# 단 1 <= s <= 4294967295
import sys
read = sys.stdin.readline
n = int(read())

for i in range(4294967295):
    sum = (i * (i+1)) // 2
    if sum > n:
        break

print(i-1)