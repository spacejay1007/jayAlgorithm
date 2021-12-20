n = int(input())

card = []

for i in range(n):
    card.append(int(input()))


card.sort()
sum = 0
for j in range(len(card) - 1):

    sum += card[j] + card[j + 1]
    card[j+1] = sum

print(sum)
# print(card[j])
# a =


# N, K = map(int, input().split())

# # N = 동전 종류
# # K = 금액가치의 합
# coin = []
# count = 0
# print(N)
# for i in range(N):
#     coin.append(int(input()))

# for j in range(N-1, -1, -1):
#     count += K // coin[j]
#     K = K % coin[j]
# print(count)
