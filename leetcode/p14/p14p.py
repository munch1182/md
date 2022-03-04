from typing import List


def longestCommonPrefix3(strs: List[str]) -> str:
    if not strs:
        return ""
    if len(strs) == 1:
        return strs[0]
    s1 = strs[0]
    for str in strs[1:-1]:
        s1


def longestCommonPrefix2(strs: List[str]) -> str:
    if not strs:
        return ""
    # min、max是根据python对ascii的排序规则获取的最小的一个值
    s1 = min(strs)
    s2 = max(strs)

    for i, x in enumerate(s1):
        if x != s2[i]:
            return s2[:i]
    return s1


def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ""
    result = strs[0]
    for str in strs:
        if result == str:
            continue
        while str.find(result) != 0:
            result = result[0:-1]
            if result == "":
                return ""
    return result


if __name__ == "__main__":
    print(longestCommonPrefix(["flower", "flow", "flight"]))
    print(longestCommonPrefix(["flower", "flow", "flow"]))
    print(longestCommonPrefix(["dog", "racecar", "car"]))
    print(longestCommonPrefix(["c", "acc", "ccc"]))
    print(longestCommonPrefix(["ac", "acc", "accc"]))
    print("------------------")
    print(longestCommonPrefix2(["flower", "flow", "flight"]))
    print(longestCommonPrefix2(["flower", "flow", "flow"]))
    print(longestCommonPrefix2(["dog", "racecar", "car"]))
    print(longestCommonPrefix2(["c", "acc", "ccc"]))
    print(longestCommonPrefix2(["ac", "acc", "accc"]))
    print(longestCommonPrefix2(["ac9", "ac91", "ac99cc"]))
