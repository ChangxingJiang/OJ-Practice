class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        ans = 0
        for i in range(32):
            if A & 1 != B & 1:
                ans += 1
            A >>= 1
            B >>= 1
        return ans


if __name__ == "__main__":
    print(Solution().convertInteger(29, 15))  # 2
    print(Solution().convertInteger(1, 2))  # 2
