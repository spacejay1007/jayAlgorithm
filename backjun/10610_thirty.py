N = input()
N = sorted(N, reverse = True)

sum = 0
for i in N:
    sum += int(i)
    print(sum)

