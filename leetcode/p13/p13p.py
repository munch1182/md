"""
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。 IV, IX
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。  XL, XC
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。 CD, CM

MCMXCIV: 1994


"""


def romanFromInt(i: int) -> str:
    # 应该使用方法而不是容器
    map = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
    list = []

    value = i
    pow = 0
    while value > 0:
        list.insert(0, value % 10 * 10**pow)
        value //= 10
        pow += 1

    def queryStr(i2: int) -> str:
        for n in map:
            if n == i2:
                return map.get(n)
            elif n > i2:
                m = n - i2
                # 用于过滤100-50=50，导致50=LC而不等于L的情形
                # 应该使用数据的方法
                if '1' not in str(m):
                    continue
                if m in map.keys():
                    return map.get(m) + map.get(n)
            else:
                return map.get(n) + queryStr(i2-n)
    s = ""
    for i in list:
        s1 = queryStr(i)
        s += s1
    return s


def romanToInt(s: str) -> int:
    map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    result = 0
    last = 0
    for i in s:
        num = map.get(i)
        result += num
        if last < num:
            result -= (num + last) - (num - last)
        last = num
    return result


if __name__ == "__main__":
    assert(romanToInt("MCMXCIV") == 1994)
    assert(romanToInt("LVIII") == 58)
    assert(romanToInt("IX") == 9)

    # print(romanFromInt(1994))
    print("58:"+romanFromInt(58))
    print("9:"+romanFromInt(9))
    print("6:"+romanFromInt(6))
    print("1591:"+romanFromInt(1591))
    print("555:"+romanFromInt(555))
    print("1994:"+romanFromInt(1994))
    print("50:"+romanFromInt(50))
    # assert(romanFromInt(1994) == "MCMXCIV")
    # assert(romanFromInt(58) == "LVIII")
    # assert(romanFromInt(9) == "IX")
