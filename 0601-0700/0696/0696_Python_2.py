class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        pre = 0
        count = 1
        curr = s[0]
        ans = 0
        for n in s[1:]:
            if n == curr:
                count += 1
            else:
                pre = count
                count = 1
                curr = n
            if pre >= count:
                ans += 1
        return ans


if __name__ == "__main__":
    print(Solution().countBinarySubstrings("0011110011"))  # 6
    print(Solution().countBinarySubstrings("111110100000"))  # 3
    print(Solution().countBinarySubstrings("00110011"))  # 6
    print(Solution().countBinarySubstrings("00100011"))  # 4
    print(Solution().countBinarySubstrings("10101"))  # 4
