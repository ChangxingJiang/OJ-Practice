class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = bin(n)
        return "11" not in n and "00" not in n


if __name__ == "__main__":
    print(Solution().hasAlternatingBits(4))  # False
    print(Solution().hasAlternatingBits(5))  # True
    print(Solution().hasAlternatingBits(7))  # False
    print(Solution().hasAlternatingBits(11))  # False
    print(Solution().hasAlternatingBits(10))  # True
