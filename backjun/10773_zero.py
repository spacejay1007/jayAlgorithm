
K = int(input())  # 몇 번 입력 받을것인가를 정하는

num = []

for i in range(K):
    addNum = int(input())   # for 문으로 다음 정수를 입력받는다
    if addNum == 0:
        num.pop()
    else:
        num.append(addNum)

print(sum(num))
