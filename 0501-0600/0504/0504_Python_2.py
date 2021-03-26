class Solution:
    def convertToBase7(self, num: int) -> str:
        minus = False
        if num < 0:
            minus = True
            num = -num

        ans = []
        while num >= 7:
            ans.append(str(num % 7))
            num //= 7
        ans.append(str(num))

        if minus:
            ans.append("-")

        ans.reverse()
        return "".join(ans)


if __name__ == "__main__":
    print(Solution().convertToBase7(100))  # 202
    print(Solution().convertToBase7(-7))  # -10
