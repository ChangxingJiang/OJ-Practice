import functools


class Solution:
    @functools.lru_cache(None)
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        elif len(s) == 1:
            return 1
        elif len(s) == 2:
            if int(s) > 26:
                return self.numDecodings(s[1:])
            else:
                return 1 + self.numDecodings(s[1:])
        elif int(s[:2]) > 26:
            return self.numDecodings(s[1:])
        else:
            return self.numDecodings(s[1:]) + self.numDecodings(s[2:])


if __name__ == "__main__":
    print(Solution().numDecodings("12"))  # 2
    print(Solution().numDecodings("226"))  # 3
    print(Solution().numDecodings("0"))  # 0
    print(Solution().numDecodings("10"))  # 1
    print(Solution().numDecodings("230"))  # 0
