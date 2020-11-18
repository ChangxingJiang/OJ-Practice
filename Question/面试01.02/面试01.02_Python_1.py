import collections


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        return collections.Counter(s1) == collections.Counter(s2)


if __name__ == "__main__":
    print(Solution().CheckPermutation(s1="abc", s2="bca"))  # True
    print(Solution().CheckPermutation(s1="abc", s2="bad"))  # False
