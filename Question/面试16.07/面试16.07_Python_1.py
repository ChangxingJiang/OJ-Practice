class Solution:
    def maximum(self, a: int, b: int) -> int:
        c = a - b
        d = c >> 63
        c = (c ^ d) - d
        return int(((a + b) + c) / 2)


if __name__ == "__main__":
    print(Solution().maximum(1, 2))  # 2
    print(Solution().maximum(2, 1))  # 2
    print(Solution().maximum(1, -2))  # 1
    print(Solution().maximum(2147483647, -2147483648))  # 2147483647
