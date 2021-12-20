N = input()
N = sorted(N, reverse=True)
print(N)
sum = 0
for i in N:
    sum += int(i)
    print(sum)
