import re


class Solution:
    def isNumber(self, s: str) -> bool:
        return re.match(r"^ *[-+]?(\d+\.?\d*|\.\d+)(e[-+]?\d+|) *$", s) is not None


if __name__ == "__main__":
    print(Solution().isNumber("0"))  # True
    print(Solution().isNumber(" 0.1 "))  # True
    print(Solution().isNumber("abc"))  # False
    print(Solution().isNumber("1 a"))  # False
    print(Solution().isNumber("2e10"))  # True
    print(Solution().isNumber(" -90e3   "))  # True
    print(Solution().isNumber(" 1e"))  # False
    print(Solution().isNumber("e3"))  # False
    print(Solution().isNumber(" 6e-1"))  # True
    print(Solution().isNumber(" 99e2.5 "))  # False
    print(Solution().isNumber("53.5e93"))  # True
    print(Solution().isNumber(" --6 "))  # False
    print(Solution().isNumber("-+3"))  # False
    print(Solution().isNumber("95a54e53"))  # False
    print(Solution().isNumber(".1"))  # True
    print(Solution().isNumber("3."))  # True
