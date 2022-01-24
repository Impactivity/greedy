import sys
read = sys.stdin.readline

n = int(read())

rope_weight = [ int(read()) for i in range(n)]

max_w = 0
for i in range(1, n+1):
    if max_w <= i * rope_weight[i-1] :
        max_w = i * rope_weight[i-1]

print(max_w)
