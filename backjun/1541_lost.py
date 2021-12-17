A = input().split("-")

num=[]

for i in A:
    # print(i)
    cnt = []
    j = i.split("+")
    for add_list in j:
        cnt += int(add_list)
    num.append(sum)

n=num[0]
print(n)
# for z in range(1, len(num)):
