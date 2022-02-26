from typing import List
from unicodedata import name


def twoSum(nums: List[int], target: int) -> List[int]:
    for i, num in enumerate(nums):
        for j, n in enumerate(nums[i::]):
            if num + n == target:
                return [i, j]
    return [-1, -1]


def twoSum2(nums: List[int], target: int) -> list[int]:
    map = {}
    for i, num in enumerate(nums):
        result = target - num
        if result in map.keys():
            return [map[result], i]
        else:
            map[num] = i

    return [-1, -1]


if __name__ == "__main__":
    print(twoSum([1, 100, 101, 104, 3], 102))
    print(twoSum([1, 10, 111, 113, 112], 112))
    
    print(twoSum2([1, 100, 101, 104, 3], 102))
    print(twoSum2([1, 10, 111, 113, 112], 112))
