class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for ch in t:
            if ch not in s:
                return ch
            else:
                s = s.replace(ch, "", 1)


if __name__ == "__main__":
    print(Solution().findTheDifference("abcd", "abcde"))  # e
    print(Solution().findTheDifference("a", "aa"))  # a
