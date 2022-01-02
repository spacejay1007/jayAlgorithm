# a,b,c = map(int,input().split())
# A = bool(int(a))
# B = bool(int(b))


# if A == B == False :
#     print(True)

# else:
#     print(False)

# if a >= b:
#     print(a)

# else:
#     print(b)

# # 최대값 출력

# if a >= b:
#     if b >= c :
#         print(b)
#     else:
#         print(c)
# else:
#     if a >= c:
#         print(a)

#     else:
#         print(c)

# 최소값 출력

# if a >= b:
#     if b >= c:
#         print(c)
#     else:
#         print(b)

# else:
#     if a >= c:
#         print(c)
#     else:
#         print(a)

# 짝수 출력
# if a % 2 == 0:
#     print("even")
# else:
#     print("odd")
# if b % 2 == 0:
#     print("even")
# else:
#     print("odd")
# if c % 2 == 0:
#     print("even")
# else:
#     print("odd")


# a = int(input())

# if a <= 0 :
#     if a % 2 == 0 :
#         print("A")
#     else:
#         print("B")
# if a >= 0:
#     if a % 2:
#         print("C")
#     else:
#         print("D")

# if a >= 90:
#     print("A")
# elif a >= 70:
#     print("B")
# elif a >= 40:
#     print("C")
# else:
#     print("D")


# a = input()

# if a == "A":
#     print("best!!!")
# elif a == "B":
#     print("good!!")
# elif a == "C":
#     print("run!")
# elif a == "D":
#     print("slowly~")
# else:
#     print("what?")

# a = int(input())

# if a // 3 == 1:
#     print("spring")
# elif a // 3 == 2:
#     print("summer")

# elif a // 3 == 3:
#     print("fall")
# else:
#     print("winter")


# while True :
#     n = int(input())
#     if int(n) == 0:
#         break
#     else:
#         print(n)

# a = int(input())


# while a != 0:
#     a -= 1
#     print(a)

# # 스펠링을 받아서 받은 스펠링 보다 낮은 스펠링 출력하기
# a = ord(input())
# t = ord("a")

# while t <= a:
#     print(chr(t), end=" ")
#     t += 1

# a = int(input())
# t = int(0)

# while a >= t:
#     print(t)
#     t += 1

# a = int(input())

# # for i in range(a+1):
#     # print(i)
# sum = 0
# for i in range(a+1):
#     if i % 2 == 0:
#         sum += i
# print(sum)


# while True:
#     a = input()
#     print(a)
#     if a == "q":
#         break

# a = int(input())
# b = 0
# # print(b)
# cnt = 0
# while a != cnt:
#     b += 1
#     cnt += b
#     if  a == cnt:
#         print(b)
#         break
#     # if a <= cnt:
#     #     break


# 주사위 경우의 수

# n, m = map(int,input().split())

# for i in range(1, n+1):
#     for j in range(1, m+1):
#         print(i,j)


# # 3의 배수는 통과

# m = int(input())

# for i in range(1, m+1):
#     if i % 3 == 0:
#         continue
#     else:
#         print(i)

# 수 나열하기 1

# a, r, n = map(int, input().split())

# x = a
# for i in range(1, n):
#     x *= r

# print(x)

# sum = 0
# for i in range(a, d+1, n):
#     sum += a[i]
#     print(sum)


# a, m, d, n = map(int, input().split())


# for i in range(1, n):
#     # print(i)

#     a = a*m+d
#     # print(sum)
# print(a)


# a, b, c = map(int, input().split())

# # a=3배수
# # b=7배수
# # c=9배수

# d = 1
# while d % a != 0 or d % b != 0 or d % c != 0:
#     d += 1

# print(d)


# a = int(input())
# b = list(map(int, input().split()))
# print(b)
# attend = []
# # for i in range(a):
# #     # print(i)
# #     b[i] = int(b[i])

# for i in range(24):
#     attend.append(0)
#     print(attend)
# for i in range(a):
#     attend[b[i]] += 1
#     # print(attend)

# for i in range(1, 24):
#     print(attend[i], end=' ')


# a = int(input())
# b = list(map(int, input().split()))

# atd = []

# # for i in range(a):
# #     b[i] = int(b[i])
# for i in range(24):
#     atd.append(0)

# for i in range(a):
#     atd[b[i]] += 1

# for i in range(1, 24):
#     print(atd[i], end=" ")


# a = int(input())
# b = list(map(int, input().split()))

# # n = sorted(b, reverse=True)

# for i in range(a-1, -1, -1):
#     print(b[i], end=" ")


# a = int(input())
# b = list(map(int, input().split()))

# b.sort()

# print(b[0])

# d = []

# for i in range(20):
#     d.append([])
#     for j in range(20):
#         d[i].append(0)

# a = int(input())

# for i in range(a):
#     x, y = map(int, input().split())
#     # print(x, y)
#     d[x][y] = 1

# for i in range(1, 20):
#     for j in range(1, 20):
#         print(d[i][j], end=" ")
#     print()

# print(d)


# a = int(input())
# for i in range(20):
#     b = list(int, input().split())
#     print(i)


# a = int(input())

# m = [10, 50, 100, 500, 1000, 5000, 10000, 50000]
# M = sorted(m, reverse=True)
# n = 0

# for i in M:
#     # n  a // m[i]
#     # n += a // M[i]
#     # print(i)
#     n += a // i

#     a = a % i


# # print(n)


# P = []
# J = []

# for i in range(3):
#     P.append(int(input()))
# for i in range(2):
#     J.append(int(input()))

# P.sort()
# J.sort()
# sum = (P[0]+J[0]) * 1.1

# print(round(sum, 1))


# # 스택 역순 출력

# a = int(input())
# n = list(map(int, input().split()))
# n.reverse()
# # N = []
# for i in n:
#     print(i, end=" ")
#     # N.append(n)

# a, b = map(int, input().split())
# c = abs(a - b)
# cnt = 0

# while c != 0:

#     if c >= 10:

#         c -= 10
#         cnt += 1
#     # print(cnt)

#     else:
#         if c <= 9 and c >= 5:

#             c -= 5
#         # a += 5
#             cnt += 1
# #         # a = a % btn[2]

#         elif c <= 4:
#             c -= 1
#             cnt += 1
# print(cnt)
# print(cnt)

# for i in True:
#     if a < b:

# for i in range(a-1, -1, -1):
#     cnt += b // btn[i]
#     b = b % btn[i]
# print(cnt)


# a, b = map(int, input().split())

# c = abs(a-b)
# cnt = 0

# while True:
#     if c == 0:
#         break
#     elif c >= 10:
#         c -= 10
#     elif c <= 9 and c >= 5:
#         c -= 5
#     elif c <= 4:
#         c -= 1
#     cnt += 1
# print(cnt)


N, K = map(int, input().split())

cup = []
c = 0


for i in range(1, N+1):
    cup.append(i)

# print(sum(cup))
# while sum(cup) >= K:
#     K = K - cup[i]
#     c += 1

for i in range(N-1, -1, -1):
    if sum(cup) >= K:
        K = K - cup[i]
        c += 1

    elif sum(cup) < K:
        c = -1


#         sum = K - cup[i]
#         c += 1
print(c)
# if sum == K:
#     break
# elif sum > K

# print(c)
# if N < K:
#     print(-1)
