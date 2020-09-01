class Solution:
    def numSteps(self, s: str) -> int:
        has_one = False
        ans = 0
        for ch in s[1:][::-1]:
            if ch == "0":
                ans += 2 if has_one else 1
            else:
                ans += 1 if has_one else 2
                has_one = True
        return ans + 1 if has_one else ans


if __name__ == "__main__":
    print(Solution().numSteps(s="1101"))  # 6
    print(Solution().numSteps(s="10"))  # 1
    print(Solution().numSteps(s="1"))  # 0
