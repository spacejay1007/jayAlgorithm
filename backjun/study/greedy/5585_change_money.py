N = 1000 - int(input())

# change = 1000 - N
change_list = [500, 100, 50, 10, 5, 1]
change_cnt = 0


for i in change_list:
    change_cnt += N // i
    print(change_cnt)
    # N
    N %= i
    # print(N)

# print(change_cnt)
