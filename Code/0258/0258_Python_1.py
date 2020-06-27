class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            ans = 0
            for c in str(num):
                ans += int(c)
            num = ans
        return num


if __name__ == "__main__":
    print(Solution().addDigits(38))  # 2
