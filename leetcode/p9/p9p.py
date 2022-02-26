def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]


def isPalindrome2(x: int) -> bool:
    if x < 0:
        return False
    list = []
    while x > 0:
        list.append(x % 10)
        x //= 10
    l = len(list)
    for i in range(l // 2):
        if list[i] != list[l - 1 - i]:
            return False
    return True


def isPalindrome3(x: int) -> bool:
    if x < 0 or (x != 0 and x % 10 == 0):
        return False
    y = 0
    while x > y:
        y = y*10 + x % 10
        x //= 10
    return x == y or y//10 == x


if __name__ == '__main__':
    print(isPalindrome(121))
    print(isPalindrome(-121))
    print(isPalindrome(1221))

    print(isPalindrome2(121))
    print(isPalindrome2(-121))
    print(isPalindrome2(1221))
    
    print(isPalindrome3(121))
    print(isPalindrome3(-121))
    print(isPalindrome3(1221))
