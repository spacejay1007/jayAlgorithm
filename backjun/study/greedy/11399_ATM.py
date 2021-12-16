N = int(input())
T = list(map(int, input().split()))
T.sort()

min_sum = 0
for i in range(N):

    min_sum += T[i]
    T[i] = min_sum

print(sum(T))
