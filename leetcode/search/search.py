
from typing import List


def serch(target: int, list: List[int]) -> tuple:
    """
    Returns:
        tuple: (该数字在集合中的序号，查找的次数)
    """
    list = sorted(list)

    left = 0
    right = len(list) - 1

    count = 1

    while(left <= right):
        mid = (left + right) // 2
        num = list[mid]

        # print(str((mid, num, target)))
        if target > num:
            left = mid + 1
        elif target < num:
            right = mid - 1
        else:
            return (mid, count)
        count += 1
    return (-1, count)


if __name__ == '__main__':
    print(serch(99, range(0, 100)))
    print(serch(200, range(0, 100000)))
    print(serch(99999, range(0, 100000)))
    print(serch(1, [1]))
    print(serch(-1, range(0, 10000000)))
    print(serch(1000001,  range(0, 1000000)))
