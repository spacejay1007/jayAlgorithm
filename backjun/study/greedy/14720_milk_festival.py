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


# n = int(input())

# if n == int(n):
#     print(True)
# else:
#     print(False)


# print('%.3f' % c)

# A = round(a, 2)
# print(A)
# print(int(a)//int(b))
# c = A ** B

# n = int(input())

# # print(n % 10 == 3)

# for i in range(1, n+1):
#     if i % 3 == 0:
#         print("X", end=" ")
#     else:
#         print(i, end=" ")2


# a = int(input())

# for i in range(1, a+1):
#     if i % 10 == 3:
#         print("X", end=" ")
#     elif i % 10 == 6:
#         print("X", end=" ")
#     elif i % 10 == 9:
#         print("X", end=" ")

#     else:
#         print(i, end=" ")

# r, g, b = map(int, input().split())

# cnt = 0

# for i in range(r):
#     for j in range(g):
#             print(i, j, k)
#             cnt += 1
#         for k in range(b):
# print(cnt)

# h, b, c, s = map(int, input().split())

# Mb = (((h*b*c*s) / 8) / 1024/1024)
# MB = round(Mb, 1)
# print(MB, "MB")

n = int(input())

cnt = 0
sum = 0

while True:
    cnt += 1
    sum += cnt
    if n <= sum:
        break
print(sum)
