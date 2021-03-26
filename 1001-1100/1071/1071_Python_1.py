class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        size1 = len(str1)
        size2 = len(str2)
        size = min(size1, size2)
        for i in range(size, 0, -1):
            k1 = size1 / i
            k2 = size2 / i
            if k1 % 1 == 0 or k2 % 1 == 0:
                if str1[:i] * int(k1) == str1 and str1[:i] * int(k2) == str2:
                    return str1[:i]
        else:
            return ""


if __name__ == "__main__":
    print(Solution().gcdOfStrings(str1="ABCABC", str2="ABC"))  # "ABC"
    print(Solution().gcdOfStrings(str1="ABABAB", str2="ABAB"))  # "AB"
    print(Solution().gcdOfStrings(str1="LEET", str2="CODE"))  # ""
