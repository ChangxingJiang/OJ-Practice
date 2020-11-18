class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        now = 0
        for ch in s:
            if ch == "(":
                now += 1
                ans = max(ans, now)
            elif ch == ")":
                now -= 1
        return ans


if __name__ == "__main__":
    print(Solution().maxDepth("(1+(2*3)+((8)/4))+1"))  # 3
    print(Solution().maxDepth("(1)+((2))+(((3)))"))  # 3
    print(Solution().maxDepth("1+(2*3)/(2-1)"))  # 1
    print(Solution().maxDepth("1"))  # 0
