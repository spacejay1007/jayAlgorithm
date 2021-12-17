N = int(input())

A_num = list(map(int,input().split()))
B_num = list(map(int,input().split()))

S = 0
A_num.sort()
for i in range(N):
    B_sort = B_num.pop(B_num.index(max(B_num)))
    
    S += A_num[i] * B_sort


print(S)


