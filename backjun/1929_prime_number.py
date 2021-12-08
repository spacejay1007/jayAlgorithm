# 소수란?
# 자기자신과 1외에는 아무것도 나눌 수 없다! (1과 자기 자신 외의 약수를 가지지 않는 1보다 큰 자연수)

# 아래의 숫자는 자신 외에는 약수를 가지지 않는 수 '소수'
# 2,3,5,7,11,13,17,18,23,29,31,37,41,43, ...

# 아래의 숫자는 1보다 큰 자연수 중 소수를 제외하면 아래의 수가 나오는데
# 1과 자기자신 이외의 수를 약수로 가지는 자연수 '합성수'

# 4,6,8,9,10,12,14,15,16,18,20, ...

# def isPrime(num): #소수점구하는 방식
#     if num == 1:
#         return False
#     else:
#         for i in range(2, int(num**0.5)+1):
#             if num % i == 0:
#                 return False
#         return True


# M, N = map(int, input().split())

# for i in range(M, N+1):
#     if isPrime(i):
#         print(i)

M, N = map(int, input().split())
arr = []

for i in range(M, N+1):
    if i == 1:
        pass
    elif i == 2:
        arr.append(i)
    else:
        for j in range(2, i):
            if i % j == 0:
                break
            elif j == i-1:
                arr.append(i)

for i in arr:
    print(i)


#에라토스테네스 체는 각 배수를 걸러내어 소수만 남게 한다.
# 소수 : 약수가 1과 자기 자신밖에 없는 자연수 (1보다 큼)
# 약수 : 어떠한 자연수를 나머지가 0으로 만드는 수