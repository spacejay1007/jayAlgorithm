
H, W, V = map(int, input().split())


floor = H % V
room = int(H/V) + 1

if floor == 0:
    floor = H
    room = room - 1

    print(floor*100+room)
