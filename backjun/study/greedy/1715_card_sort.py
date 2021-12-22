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

