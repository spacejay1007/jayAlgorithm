n = list(input())
n.sort(reverse=True)

sum = 0
for i in n:
    # print(int(i))

    sum += int(i)

thirty = "".join(n)
# print(thirty)
if int(thirty) % 30 != 0:
    print(-1)

else:
    print(thirty)
# print(thirty)


# n = list(input())
# n.sort(reverse=True)
# sum = 0
# for i in n:
#     sum += int(i)
# if sum % 3 != 0 or "0" not in n:
#     print(-1)
# else:
#     print(''.join(n))

# for i in range(n):


# thirty = []
# if thirty % 30 != 0:
#     print(-1)
