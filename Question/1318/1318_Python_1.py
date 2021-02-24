class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0

        length = max(a.bit_length(), b.bit_length(), c.bit_length())
        for i in range(length):
            if c & (1 << i):
                if not a & (1 << i) and not b & (1 << i):
                    ans += 1
            else:
                if a & (1 << i):
                    ans += 1
                if b & (1 << i):
                    ans += 1

        return ans


if __name__ == "__main__":
    print(Solution().minFlips(2, 6, 5))  # 3
    print(Solution().minFlips(4, 2, 7))  # 1
    print(Solution().minFlips(1, 2, 3))  # 0
    print(Solution().minFlips(1, 2, 3))  # 0
    print(Solution().minFlips(7, 7, 7))  # 0
