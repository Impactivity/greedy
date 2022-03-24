def solution(n, costs):
    costs.sort(key = lambda k : k[2]) # 비용기준으로 오름차순 정렬
    nodes = set([costs[0][0]]) # 섬 간 연결을 확인하는 집합
    answer = 0
    # Kruskal 알고리즘으로 최소 비용 구하기
    while len(nodes) != n:
        for cost in costs:
            if cost[0] in nodes and cost[1] in nodes:
                continue
            if cost[0] in nodes or cost[1] in nodes:
                nodes.update([cost[0],cost[1]])
                answer += cost[2]
                break

    return answer

costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
n = 4
solution(n,costs)