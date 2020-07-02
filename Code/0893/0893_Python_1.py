from typing import List


class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        def helper(s):
            odd = "".join(sorted(list([s[i] for i in range(len(s)) if i % 2 == 0])))
            even = "".join(sorted(list([s[i] for i in range(len(s)) if i % 2 == 1])))
            return odd + even
        return len(set([helper(a) for a in A]))


if __name__ == "__main__":
    print(Solution().numSpecialEquivGroups(["a", "b", "c", "a", "c", "c"]))  # 3
    print(Solution().numSpecialEquivGroups(["aa", "bb", "ab", "ba"]))  # 4
    print(Solution().numSpecialEquivGroups(["abc", "acb", "bac", "bca", "cab", "cba"]))  # 3
    print(Solution().numSpecialEquivGroups(["abcd", "cdab", "adcb", "cbad"]))  # 1
