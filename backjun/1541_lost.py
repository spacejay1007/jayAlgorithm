a = input().split('-')
num = []
for i in a:
    cnt = 0
    s = i.split('+')
    print(i)
    print(s)
    for j in s:
        cnt += int(j)
    num.append(cnt)
    print(num)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)
