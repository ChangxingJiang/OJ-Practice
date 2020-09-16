class Solution:
    def maxPower(self, s: str) -> int:
        last = s[0]
        start = 0
        ans = 0
        for i in range(1, len(s)):
            if s[i] != last:
                ans = max(ans, i - start)
                last = s[i]
                start = i
        else:
            ans = max(ans, len(s) - start)

        return ans


if __name__ == "__main__":
    print(Solution().maxPower(s="leetcode"))  # 2
    print(Solution().maxPower(s="abbcccddddeeeeedcba"))  # 5
    print(Solution().maxPower(s="triplepillooooow"))  # 5
    print(Solution().maxPower(s="hooraaaaaaaaaaay"))  # 11
    print(Solution().maxPower(s="tourist"))  # 1
    print(Solution().maxPower(s="a"))  # 1
