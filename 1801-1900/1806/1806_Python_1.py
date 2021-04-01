class Solution:
    def reinitializePermutation(self, n: int) -> int:
        if n == 2:
            return 1

        # 判断数字1的位置
        ans = 1
        now = 2
        while now != 1:
            if now < n // 2:
                now *= 2
                ans += 1
            else:
                now = (now - n // 2) * 2 + 1
                ans += 1
        return ans


if __name__ == "__main__":
    print(Solution().reinitializePermutation(2))  # 1
    print(Solution().reinitializePermutation(4))  # 2
    print(Solution().reinitializePermutation(6))  # 4
    print(Solution().reinitializePermutation(8))  # 3
