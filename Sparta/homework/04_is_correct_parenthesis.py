s = "(())()"


def is_correct_parenthesis(string):
    stack = []

    for i in range(len(string)):  # string 의 길이 만큼 볼거다
        # print(i)
        if string[i] == "(":
            stack.append(i)
        # print(stack)
        elif string[i] == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
        # print(stack)
    if len(stack) == 0:
        return True

    else:
        return False


print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!

# s = "(())()"


# def is_correct_parenthesis(string):
#     # 구현해보세요!
#     cnt_sum = 0
#     for string in s:
#         if string == "(":
#             cnt_sum += 1

#         if string == ")":
#             cnt_sum -= 1

#     if cnt_sum < 0:
#         s == "True"

#     elif cnt_sum != 0:
#         s == "False"


# print(is_correct_parenthesis(s))  # True 를 반환해야 합니다!
