class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        num0 = 0
        num1 = 0
        ans = 0
        for i in range(len(s)):
            n = s[i]
            if i > 0 and s[i] != s[i - 1]:
                if s[i] == "0":
                    num0 = 0
                else:
                    num1 = 0
            if n == "1":
                if num0 > 0:
                    ans += 1
                    num0 -= 1
                num1 += 1
            elif n == "0":
                if num1 > 0:
                    ans += 1
                    num1 -= 1
                num0 += 1
        return ans


if __name__ == "__main__":
    print(Solution().countBinarySubstrings("0011110011"))  # 6
    print(Solution().countBinarySubstrings("111110100000"))  # 3
    print(Solution().countBinarySubstrings("00110011"))  # 6
    print(Solution().countBinarySubstrings("00100011"))  # 4
    print(Solution().countBinarySubstrings("10101"))  # 4
