A = input().split("-")

<<<<<<< HEAD
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
=======
total = 0

for i in A[0].split("+"):
    total += int(i)

for i in A[1:]:
    for j in i.split("+"):
        total -= int(j)

print(total)
>>>>>>> 80a7a1e604703c95aa7c8040fe85a32cf0f96b26
