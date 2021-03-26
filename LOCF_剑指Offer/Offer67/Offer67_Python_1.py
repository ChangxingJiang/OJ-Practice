import re


class Solution:
    def strToInt(self, str: str) -> int:
        if ans := re.search("^[-+]?[0-9]+", str.lstrip()):
            ans = int(ans.group())
            if ans > 2147483647:
                return 2147483647
            elif ans < -2147483648:
                return -2147483648
            else:
                return ans
        else:
            return 0


if __name__ == "__main__":
    print(Solution().strToInt("+1"))  # 1
    print(Solution().strToInt("42"))  # 42
    print(Solution().strToInt("   -42"))  # -42
    print(Solution().strToInt("4193 with words"))  # 4193
    print(Solution().strToInt("words and 987"))  # 0
    print(Solution().strToInt("-91283472332"))  # -2147483648
