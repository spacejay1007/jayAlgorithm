def solution(board, moves):
    answer = 0
    bucket = []

    # move 는 index 가 아니기 때문에 index 로 변화해줘야함
    for move in moves:
        index = move - 1  # moves는 몇 번째로 되어있기 때문에 index가 아니다 그래서 index로 변경
        for j in board:  # board 가 비어있는지 안비었는지 확인하는 for문
            if j[index] != 0:
                bucket.append(j[index])
                j[index] = 0  # 번호가 뽑혀갔을때 0으로 만들어 줘야한다.

                if len(bucket) >= 2 and bucket[-1] == bucket[-2]
                answer += 2
                bucket = bucket[:-2]

                break

    return answer
