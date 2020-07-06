class Solution:
    def balancedStringSplit(self, s: str) -> int:
        num = 0
        ans = 0
        for c in s:
            if c == "L":
                num -= 1
            if c == "R":
                num += 1
            if num == 0:
                ans += 1
        return ans


if __name__ == "__main__":
    print(Solution().balancedStringSplit("RLRRLLRLRL"))  # 4
    print(Solution().balancedStringSplit("RLLLLRRRLR"))  # 3
    print(Solution().balancedStringSplit("LLLLRRRR"))  # 1
