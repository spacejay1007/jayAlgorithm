N, K = map(int, input().split())

# N = 동전 종류
# K = 금액가치의 합
coin = []
count = 0

for i in range(N):
    coin.append(int(input()))

for j in range(N-1, -1, -1):
    count += K // coin[j]
    K = K % coin[j]
print(count)
# print(K)
