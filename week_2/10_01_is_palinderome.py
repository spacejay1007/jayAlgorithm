input = "abcba"


def is_palindrome(string):
    n = len(string)
    for i in range(n):  # i 는 0 부터 n-1 까지 반복이 된다.
        if string[i] != string[n-1 - i]:
            return False
    return True


print(is_palindrome(input))
