from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        pass


if __name__ == "__main__":
    # 16
    print(Solution().maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))

    # 4
    print(Solution().maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))

    # 0
    print(Solution().maxProduct(["a", "aa", "aaa", "aaaa"]))
