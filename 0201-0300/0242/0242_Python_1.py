import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)


if __name__ == "__main__":
    # True
    print(Solution().isAnagram(s="anagram", t="nagaram"))

    # False
    print(Solution().isAnagram(s="rat", t="car"))
