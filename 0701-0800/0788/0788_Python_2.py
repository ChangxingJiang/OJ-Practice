class Solution:
    def rotatedDigits(self, N: int) -> int:
        ans = 0
        for i in range(1, N + 1):
            s = str(i)
            differ = False
            for c in s:
                if c in ["2", "5", "6", "9"]:
                    differ = True
                elif c in ["3", "4", "7"]:
                    break
            else:
                if differ:
                    ans += 1
        return ans


if __name__ == "__main__":
    print(Solution().rotatedDigits(10))  # 4
    print(Solution().rotatedDigits(120))  # 4

