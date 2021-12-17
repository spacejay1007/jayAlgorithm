# N = int(input())
# S = list(map(int, input().split()))

# # print(N, S)
# cnt = 0

# for i in range(N):
#     C = cnt % 3
#     if S[i] == C:
#         cnt += 1


# print(cnt)
# # cnt = cnt // 3
# # print(cnt)

a, b = map(int, input().split())

if a < b:
    print(True)
elif a >= b:
    print(False)


# print('%.3f' % c)

# A = round(a, 2)
# print(A)
# print(int(a)//int(b))
# c = A ** B
