from typing import List


class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().numSpecialEquivGroups(["a", "b", "c", "a", "c", "c"]))  # 3
    print(Solution().numSpecialEquivGroups(["aa", "bb", "ab", "ba"]))  # 4
    print(Solution().numSpecialEquivGroups(["abc", "acb", "bac", "bca", "cab", "cba"]))  # 3
    print(Solution().numSpecialEquivGroups(["abcd", "cdab", "adcb", "cbad"]))  # 1
