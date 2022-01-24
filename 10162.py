import sys

read = sys.stdin.readline

t = int(read())
timer = [300,60,10]

# solution 1 메모리 30864 kb , 시간 76ms
# if t % timer[2] != 0:
#     print(-1)
# else:
#     A = t // timer[0]
#     B = (t % timer[0]) // timer[1]
#     C = ((t % timer[0]) % timer[1]) // timer[2]
#     print(A,B,C)

# solution 2 메모리 : 30864 kb, 시간 : 72 ms
cnt = [0, 0, 0]

while t > 0:
    if t % timer[2] != 0:
        print(-1)
        exit(0)
    else:
        if t >= timer[0]:
            t = t - timer[0]
            cnt[0] += 1
        elif t >= timer[1] and t < timer[0]:
            t = t - timer[1]
            cnt[1] += 1
        elif t >= timer[2] and t < timer[1]:
            t = t - timer[2]
            cnt[2] += 1

for i in cnt:
    print(i, end=' ')




