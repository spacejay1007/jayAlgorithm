T = int(input())

for i in range(T):
    newIn = input()
    VPS = list(newIn)
    count = 0
    for j in VPS:
        if j == "(":
            count += 1
            # VPS.append(j)

        elif j == ")":
            count -= 1
            # VPS.pop()
        if count < 0:
            print("No")
            break
    if count > 0:
        print("No")
    elif count == 0:
        print("Yes")
