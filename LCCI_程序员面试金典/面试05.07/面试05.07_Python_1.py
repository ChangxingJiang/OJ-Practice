class Solution:
    def exchangeBits(self, num: int) -> int:
        p1, p2 = int("10101010101010101010101010101010", base=2), int("01010101010101010101010101010101", base=2)
        n1 = num & p1  # 所有偶数位
        n2 = num & p2  # 所有奇数位
        return (n1 >> 1) | (n2 << 1)


if __name__ == "__main__":
    print(Solution().exchangeBits(2))  # 1
    print(Solution().exchangeBits(3))  # 3
    print(Solution().exchangeBits(1))  # 2
    print(Solution().exchangeBits(571603718))  # 287504137
