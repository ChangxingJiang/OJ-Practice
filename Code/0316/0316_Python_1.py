from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s:
            return ""
        count = Counter(s)
        pos = 0
        for i in range(len(s)):
            if s[i] < s[pos]:
                pos = i
            count[s[i]] -= 1
            if count[s[i]] == 0:
                break
        return s[pos] + self.removeDuplicateLetters(s[pos:].replace(s[pos], ""))


if __name__ == "__main__":
    print(Solution().removeDuplicateLetters("bcabc"))  # "abc"
    print(Solution().removeDuplicateLetters("cbacdcbc"))  # "acdb"
    print(Solution().removeDuplicateLetters("abacb"))  # "abc"
