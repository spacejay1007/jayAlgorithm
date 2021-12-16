input = [4, 6, 2, 9, 1]


def selection_sort(array):
    # 이 부분을 채워보세요!
    n = len(array)

    for i in range(n - 1):
        min_index = i  # 최소값을 찾아서 변경해서 찾아주는 조건
        for j in range(n - i):
            # 시도해보고 있는 index = if array[i+j]
            if array[i+j] < array[min_index]:
                min_index = i+j
        array[i], array[min_index] = array[min_index], array[i]

    return


selection_sort(input)
print(input)  # [1, 2, 4, 6, 9] 가 되어야 합니다!
