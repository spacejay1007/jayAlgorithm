N = int(input())

T = []
for i in range(N):
    T += tuple(map(int, input().split()))
    print(T)
