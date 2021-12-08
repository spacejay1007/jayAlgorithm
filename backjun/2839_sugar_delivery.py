N = int(input())
delivery = 0

while N >= 0:
    if N % 5 == 0:
        delivery = delivery + int(N // 5)
        print(delivery)
        break

    N = N - 3
    delivery = delivery + 1

else:
    print(-1)
