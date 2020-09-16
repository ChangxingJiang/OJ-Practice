class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = n ^ (n << 1)  # -> 1...10 or 1...11
        n = n >> 1  # -> 1..11
        return n & (n + 1) == 0


if __name__ == "__main__":
    print(Solution().hasAlternatingBits(4))  # False
    print(Solution().hasAlternatingBits(5))  # True
    print(Solution().hasAlternatingBits(7))  # False
    print(Solution().hasAlternatingBits(11))  # False
    print(Solution().hasAlternatingBits(10))  # True
