class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        size = len(s)
        next = [-1] * size
        for i in range(1, size):
            j = next[i - 1]
            while j >= 0 and s[j + 1] != s[i]:
                j = next[j]
            if s[j + 1] == s[i]:
                next[i] = j + 1
        return next[-1] >= 0 and size % (size - 1 - next[-1]) == 0


if __name__ == "__main__":
    print(Solution().repeatedSubstringPattern("ababacbaba"))  # True
    print(Solution().repeatedSubstringPattern("abab"))  # True
    print(Solution().repeatedSubstringPattern("aba"))  # False
    print(Solution().repeatedSubstringPattern("abcabcabcabc"))  # True
    print(Solution().repeatedSubstringPattern("a"))  # False
