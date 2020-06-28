class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        size = len(s)
        for i in range(1, size // 2 + 1):
            # 若不是子串长度的整倍数则一定不是该长度子串的多次构成
            if size % i != 0:
                continue
            # 比较各部分子串是否相同
            if (s[:i] * (size // i)) == s:
                return True
        else:
            return False


if __name__ == "__main__":
    print(Solution().repeatedSubstringPattern("abab"))  # True
    print(Solution().repeatedSubstringPattern("aba"))  # False
    print(Solution().repeatedSubstringPattern("abcabcabcabc"))  # True
    print(Solution().repeatedSubstringPattern("a"))  # False
