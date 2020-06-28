class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        size = len(s)
        for i in range(1, size):
            # 若不是子串长度的整倍数则一定不是该长度子串的多次构成
            if size % i != 0:
                continue

            # 比较各部分子串是否相同
            differ = False
            pattern = s[:i]
            for j in range(1, size // i):
                sample = s[j * i:(j + 1) * i]
                if pattern != sample:
                    differ = True
                    break
            if not differ:
                return True
        else:
            return False


if __name__ == "__main__":
    print(Solution().repeatedSubstringPattern("abab"))  # True
    print(Solution().repeatedSubstringPattern("aba"))  # False
    print(Solution().repeatedSubstringPattern("abcabcabcabc"))  # True
