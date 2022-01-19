import sys
read = sys.stdin.readline
n = int(read())

room = [ list(map(int, read().split())) for _ in range(n)]


# solution 1 bfs로 가능한 경우의 수 모두 탐색, -> 시간초과
# _max_count = 0
# def dfs(depth, count, cur_room):
#     global _max_count
#     start_time, end_time = cur_room
#
#     if depth > n-1:
#         return
#
#     for time in range(depth+1,n):
#         if end_time <= room[time][0]:
#             _max_count = max(_max_count,count+1)
#             dfs(time , count+1, room[time]) # 현재 회의실 선택 했다고 가정할 때
#
#             dfs(time+1, count, cur_room) # 현재 회의실을 스킵한다고 가정할 때(다른 경우의 수 조사)
#             #이전 회의실부터 다시 조사하려면 dfs함수 인자에서 현재 회의실을 넘겨줄수있는 인자가 필요함.
#     return
#
# dfs(0,1,room[0])
# print(_max_count)


# solution 2
room.sort(key=lambda k:(k[1] , k[0]))
end_time = room[0][1]
count = 1
for time in range(1,n):
    if end_time <= room[time][0]:
        count += 1
        end_time = room[time][1]

print(count)