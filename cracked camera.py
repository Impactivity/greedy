
def solution(routes):
    answer = 0
    # 진출 위치 기준으로 정렬
    routes.sort(key=lambda k: k[1])
    camera = -30001

    # 카메라 위치 재 설정
    for route in routes:
        if camera < route[0]:
            answer += 1
            camera = route[1]

    return answer