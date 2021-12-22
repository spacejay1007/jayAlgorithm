# S = int(input())
s = int(input())
n = 1
while n * (n + 1) / 2 <= s:
    n += 1
    print(n)
print(n - 1)

# while n <= s:

#     n += 1

# print(n)
# print(cnt)
