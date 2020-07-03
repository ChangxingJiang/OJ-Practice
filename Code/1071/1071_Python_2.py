import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        size = math.gcd(len(str1), len(str2))
        if str1 + str2 == str2 + str1:
            return str1[: size]
        return ""


if __name__ == "__main__":
    print(Solution().gcdOfStrings(str1="ABCABC", str2="ABC"))  # "ABC"
    print(Solution().gcdOfStrings(str1="ABABAB", str2="ABAB"))  # "AB"
    print(Solution().gcdOfStrings(str1="ABABAB", str2="ABABAB"))  # "AB"
    print(Solution().gcdOfStrings(str1="LEET", str2="CODE"))  # ""
