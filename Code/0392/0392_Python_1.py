class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for c in s:
            if c in t:
                t = t[t.index(c) + 1:]
            else:
                return False
        else:
            return True


if __name__ == "__main__":
    print(Solution().isSubsequence("abc", "ahbgdc"))  # True
    print(Solution().isSubsequence("axc", "ahbgdc"))  # False
    print(Solution().isSubsequence("aaaaaa", "bbaaaa"))  # False
    print(Solution().isSubsequence("bb", "ahbgdc"))  # False
