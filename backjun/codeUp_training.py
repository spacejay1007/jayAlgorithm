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
for i in range(20):
    b = list(int, input().split())
    print(i)
