def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    # 이 부분을 채워보세요!
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array))
    alphabet_occurrence = alphabet_occurrence_array[index]

    if alpjabet_occurrence > max_occurrence:
        max_alphabet_index = index
        max_occurrence = alphabet_occurrence_array
    print(index)
    return alphabet_occurrence_array


result = find_max_occurred_alphabet
print("정답 = a 현재 풀이 값 =", result("Hello my name is sparta"))
print("정답 = a 현재 풀이 값 =", result("Sparta coding club"))
print("정답 = s 현재 풀이 값 =", result("best of best sparta"))
