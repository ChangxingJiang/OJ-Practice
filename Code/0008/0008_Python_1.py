import re


class Solution:
    def myAtoi(self, str: str) -> int:
        # 字符串格式预处理
        match = re.search(r"^[+-]?[0-9]+", str.lstrip())

        # 处理没有匹配结果的情况
        if not match:
            return 0

        # 处理包含匹配结果的情况
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1

        group = int(match.group())
        if group < INT_MIN:
            return INT_MIN
        elif group > INT_MAX:
            return INT_MAX
        else:
            return group


if __name__ == "__main__":
    print(Solution().myAtoi("42"))  # 42
    print(Solution().myAtoi("   -42"))  # -42
    print(Solution().myAtoi("4193 with words"))  # 4193
    print(Solution().myAtoi("words and 987"))  # 0
    print(Solution().myAtoi("-91283472332"))  # -2147483648
    print(Solution().myAtoi("+1"))  # 1
    print(Solution().myAtoi("  0000000000012345678"))  # 12345678
    print(Solution().myAtoi("-000000000000000001"))  # -1
    print(Solution().myAtoi("   +0 123"))  # 0
    print(Solution().myAtoi("0-1"))  # 0
    print(Solution().myAtoi("010"))  # 10
