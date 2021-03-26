class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        for i in range(1, len(s)):
            ans = max(ans, s[0:i].count("0") + s[i:].count("1"))
        return ans


if __name__ == "__main__":
    print(Solution().maxScore(s="011101"))  # 5
    print(Solution().maxScore(s="00111"))  # 5
    print(Solution().maxScore(s="1111"))  # 3
