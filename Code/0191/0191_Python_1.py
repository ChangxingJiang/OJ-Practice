class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        for s in "{:032b}".format(n):
            if s == "1":
                ans += 1
        return ans


if __name__ == "__main__":
    print(Solution().hammingWeight(int("0b00000000000000000000000000001011", 2)))  # 3
    print(Solution().hammingWeight(int("0b00000000000000000000000010000000", 2)))  # 1
    print(Solution().hammingWeight(int("0b11111111111111111111111111111101", 2)))  # 31
