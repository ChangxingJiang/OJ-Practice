class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        N = len(s)
        arr = [0] * N
        i = 1
        j = 0
        while i < N:
            if s[i] == s[j]:
                j += 1
                arr[i] = j
                i += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = arr[j - 1]
        return arr[-1] > 0 and N % (N - arr[-1]) == 0


if __name__ == "__main__":
    print(Solution().repeatedSubstringPattern("ababacbaba"))  # False
    print(Solution().repeatedSubstringPattern("abab"))  # True
    print(Solution().repeatedSubstringPattern("aba"))  # False
    print(Solution().repeatedSubstringPattern("abcabcabcabc"))  # True
    print(Solution().repeatedSubstringPattern("a"))  # False
    print(Solution().repeatedSubstringPattern("ababba"))  # False
