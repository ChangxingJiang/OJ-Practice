class Solution:
    def maxScore(self, s: str) -> int:
        a = 0
        for c in s:
            if c == "1":
                a += 1

        ans = 0

        b = 0
        for c in s[:-1]:
            if c == "0":
                b += 1
                ans = max(ans, a + b)
            else:
                a -= 1
                ans = max(ans, a + b)

        return ans


if __name__ == "__main__":
    print(Solution().maxScore(s="011101"))  # 5
    print(Solution().maxScore(s="00111"))  # 5
    print(Solution().maxScore(s="1111"))  # 3
