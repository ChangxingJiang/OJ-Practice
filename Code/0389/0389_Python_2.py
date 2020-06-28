import collections


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return list((collections.Counter(t)-collections.Counter(s)).keys())[0]


if __name__ == "__main__":
    print(Solution().findTheDifference("abcd", "abcde"))  # e
    print(Solution().findTheDifference("a", "aa"))  # a
