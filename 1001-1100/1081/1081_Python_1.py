import collections


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        if not s:
            return ""
        count = collections.Counter(s)
        pos = 0
        for i in range(len(s)):
            if s[i] < s[pos]:
                pos = i
            count[s[i]] -= 1
            if count[s[i]] == 0:
                break
        return s[pos] + self.smallestSubsequence(s[pos:].replace(s[pos], ""))


if __name__ == "__main__":
    print(Solution().smallestSubsequence("cdadabcc"))  # "adbc"
    print(Solution().smallestSubsequence("abcd"))  # "abcd"
    print(Solution().smallestSubsequence("ecbacba"))  # "eacb"
    print(Solution().smallestSubsequence("leetcode"))  # "letcod"
