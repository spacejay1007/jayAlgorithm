A = int(input())

num = A
cnt = 0

while True:
    a = num // 10
    b = num % 10
    c = (a + b) % 10

    num = (b * 10) + c
    print(num)
    cnt += 1

    if A == num:

        break

print(cnt)
