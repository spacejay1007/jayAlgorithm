input = [0, 3, 5, 6, 1, 2, 4]

0 + 3 = 3
3 * 5 = 15
15 * 6 = 90
90 + 1 = 91
91 * 2 = 182
182 * 4 = 728


def find_max_plus_or_multiply(array):
    multiply_sum = 0
    for number in array:
        if number <= 1 or multiply_sum <= 1:
            multiply_sum += number
        else:
            multiply_sum *= number
    return multiply_sum


result = find_max_plus_or_multiply(input)
print(result)
