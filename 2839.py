import sys
read = sys.stdin.readline

n = int(read())
# solution 1  메모리 : 30864 kb, 시간 68ms

cnt = 0

while n >= 0 :
    if n % 5 == 0: # 5키로그램으로 나누어 떨어진다면
        cnt += n // 5
        print(cnt)
        exit(0)
    else: # 나누어 떨어지지 않을 떄 3키로 먼저 제거하고 나머지로 계산한다.
        n = n - 3
        cnt += 1

else :
    print(-1)




# solution 2  메모리 : 30864 kb , 시간 68ms
# sugar = [5,3]
#
# min_cnt = 999999
# cnt = 0
#
# #5키로로 나누어지는 경우
# if n % sugar[0] == 0:
#     cnt += n // sugar[0]
#     print(cnt)
# else : # 첫번째 5키로로 나누어 떨어지지 않는 경우
#     inx = 0
#
#     while sugar[0]*inx < n :
#         cnt = 0
#         # inx 수 만큼 5키로그램 짜리 사탕을 뺸다.
#         tmp = ( n - sugar[0]*inx )
#
#         if tmp % sugar[1] == 0:
#             cnt += tmp // sugar[1]
#             if inx != 0 : # 0이아닐때 처음에 뺀 5키로 수 inx 만큼 더해준다.
#                 cnt += inx
#             min_cnt = min(cnt, min_cnt)
#         inx += 1
#
#     if min_cnt == 999999:
#         print(-1)
#     else:
#         print(min_cnt)
#
#


