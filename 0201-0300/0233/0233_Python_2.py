class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = 0
        high = n
        low = 0
        digit = 1
        while high > 0:
            high, curr = divmod(high, 10)

            if curr == 0:
                ans += high * digit
            elif curr == 1:
                ans += high * digit + low + 1
            else:
                ans += high * digit + digit

            # print(high, curr, low)

            low = low + curr * digit
            digit *= 10

        return ans


if __name__ == "__main__":
    print(Solution().countDigitOne(13))  # 6
    print(Solution().countDigitOne(-1))  # 0
    print(Solution().countDigitOne(101))  # 23
