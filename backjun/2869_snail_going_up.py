
A, B, V = map(int, input().split())

day = (V-B) // (A-B)

if (V-B) % (A-B) == 0:
    print(int(day))
else:
    print(int(day)+1)
