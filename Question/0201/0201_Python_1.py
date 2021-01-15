class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        ans = 0
        for i in range(n.bit_length()):
            bit1 = 1 << i
            bit2 = bit1 << 1
            if n - m < bit1 and n % bit2 >= bit1 and m % bit2 >= bit1:
                ans += n & bit1
        return ans


if __name__ == "__main__":
    print(Solution().rangeBitwiseAnd(5, 7))  # 4
    print(Solution().rangeBitwiseAnd(0, 1))  # 0
    print(Solution().rangeBitwiseAnd(0, 4))  # 0
    print(Solution().rangeBitwiseAnd(0, 6))  # 0
    print(Solution().rangeBitwiseAnd(1, 1))  # 1
