class Solution:
    def convertToBase7(self, num: int) -> str:
        if num > 0:
            ans = ""
            while num > 0:
                ans += str(num % 7)
                num //= 7
            return ans[::-1]
        elif num == 0:
            return "0"
        else:
            num = abs(num)
            ans = ""
            while num > 0:
                ans += str(num % 7)
                num //= 7
            return "-" + ans[::-1]


if __name__ == "__main__":
    print(Solution().convertToBase7(100))  # 202
    print(Solution().convertToBase7(-7))  # -10
