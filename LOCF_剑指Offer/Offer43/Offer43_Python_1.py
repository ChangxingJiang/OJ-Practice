class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = 0

        s = str(n)
        for i, ch in enumerate(s):
            high = int(s[:i]) if i > 0 else 0  # 当前位左侧数值
            curr = int(ch)  # 当前位数值
            low = int(s[i + 1:]) if i + 1 < len(s) else 0  # 当前位右侧数值
            digit = 10 ** (len(s) - i - 1)  # 当前位位数

            if curr == 0:
                ans += high * digit
            elif curr == 1:
                ans += high * digit + low + 1
            else:
                ans += high * digit + digit

        return ans


if __name__ == "__main__":
    print(Solution().countDigitOne(12))  # 5
    print(Solution().countDigitOne(13))  # 6
    print(Solution().countDigitOne(100))  # 21
