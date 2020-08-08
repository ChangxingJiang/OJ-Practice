class Solution:
    def myAtoi(self, str: str) -> int:
        pass


if __name__ == "__main__":
    print(Solution().myAtoi("42"))  # 42
    print(Solution().myAtoi("   -42"))  # -42
    print(Solution().myAtoi("4193 with words"))  # 4193
    print(Solution().myAtoi("words and 987"))  # 0
    print(Solution().myAtoi("-91283472332"))  # -2147483648
