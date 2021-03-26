class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, base=2)
        ans = 0
        while num > 1:
            if num % 2 == 1:
                num += 1
                ans += 1
            else:
                num //= 2
                ans += 1
        return ans


if __name__ == "__main__":
    print(Solution().numSteps(s="1101"))  # 6
    print(Solution().numSteps(s="10"))  # 1
    print(Solution().numSteps(s="1"))  # 0
