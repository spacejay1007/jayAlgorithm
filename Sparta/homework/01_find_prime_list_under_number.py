# Q. 정수를 입력 했을 때, 그 정수(number) 이하의 소수를 모두 반환하시오.
# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.

# range(max)
# range(min, max)
# range(min, max , gab(min+gab))

## 기본 ##
# input = 20

# def find_prime_list_under_number(number):
#     prime_list = []
#     for n in range(2, number + 1):  # 2~ number + 1 이 n에 대입 (n의 범위는 2 ~ number)
#         # print(n)
#         for i in range(2, n): # 범위 2 ~ n-1 까지
#             if n % i == 0:
#                 break
#         else:
#             prime_list.append(n)

#     return prime_list


# result = find_prime_list_under_number(input)
# print(result)

# ## 개선사항 1번
# input = 20
# # n = 19
# # i = 1,2,3,4,5,6,7,8 ... 19
# # 2 -> x / 3-> X  2와 3으로도 나누어지지 않으면 합성수인 6으로도 나누어지지 않음
# # i 를 굳이 2,3,4,5,6,7,8 할 필요 없이 소수만 적용하면 된다.


# def find_prime_list_under_number(number):
#     prime_list = []
#     for n in range(2, number + 1):  # 2~ number + 1 이 n에 대입 (n의 범위는 2 ~ number)
#         # print(n)
#         for i in prime_list:  # i의 범위 : 2부터 n-1 까지의 소수를 넣어준다.
#             if n % i == 0:
#                 break
#         else:
#             prime_list.append(n)

#     return prime_list


# result = find_prime_list_under_number(input)
# print(result)


# 개선사항 3번
input = 20

# 주어진 자연수 N이 소수이기 위하 필요 충분 조건은
# N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다.
# 수가 수를 나누면 몫이 발행하는데, 몫과 나누는 수는 둘 중 하나는 반드시 Ndml 제곱근 이하이다.


def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number + 1):  # 2~ number + 1 이 n에 대입 (n의 범위는 2 ~ number)
        # print(n)
        for i in prime_list:  # i의 범위 : 2부터 n-1 까지의 소수를 넣어준다.
            if n % i == 0 and i * i <= n:
                break
        else:
            prime_list.append(n)

    return prime_list


result = find_prime_list_under_number(input)
print(result)
