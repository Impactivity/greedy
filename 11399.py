# 문제의 핵심은 인출하는데 걸리는 시간이 배열로 주어졌을떄
# 빨리 걸리는 사람을 앞으로 배치하면 각 사람이 인출하는데 걸리는 시간의 합이 최소값이 된다는 것이다.

import sys

read = sys.stdin.readline

n = int(read())

arr = list(map(int,read().split()))
arr.sort()
tmp_sum = []

for i in range(n):
    tmp_sum.append(sum(arr[:i+1]))

print(sum(tmp_sum))