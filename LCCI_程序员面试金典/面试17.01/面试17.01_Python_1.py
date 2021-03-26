class Solution:
    def add(self, a: int, b: int) -> int:
        while b:
            a &= 0xFFFFFFFF
            b &= 0xFFFFFFFF
            a, b = a ^ b, (a & b) << 1  # 每位相加结果、进位值
        return a if a < 0x80000000 else ~(a ^ 0xFFFFFFFF)


if __name__ == "__main__":
    print(Solution().add(1, 1))  # 2
    print(Solution().add(-1, 2))  # 2
    print(Solution().add(1, -2))  # 1
