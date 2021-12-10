top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    answer = [0] * len(heights)  # heights 의 길이 만큼 0으로 초기화
    while heights:
        height = heights.pop()
        for idx in range(len(heights) - 1, 0, -1):
            # 현재 heights의 idx 부분이 height 보다 크다면 (레이저가 들어가는 순간)
            if heights[idx] > height:
                answer[len(heights)] = idx + 1
                break

    return answer


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!
