import sys
read = sys.stdin.readline

n = int(read())
A = list(map(int, read().split()))
B = list(map(int, read().split()))

A.sort()
B.sort(reverse=True)

_sum = 0
for i in range(n):
    _sum += A[i] * B[i]
print(_sum)

