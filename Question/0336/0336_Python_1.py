import collections
from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # 计算所有可以通过连接构成回文串的可能
        def all_palindromes(s: str):
            maybe_set = set()
            for i in range(len(s) + 1):
                t = s[i:][::-1] + s
                if t == t[::-1]:
                    maybe_set.add((s[i:][::-1], True))
                t = s + s[:i][::-1]
                if t == t[::-1]:
                    maybe_set.add((s[:i][::-1], False))
            return maybe_set

        maybe_dict = collections.defaultdict(list)  # 可能字典

        # 将当前可能添加到可能字典
        # 时间复杂度：N×C
        for i, word in enumerate(words):
            for maybe, orient in all_palindromes(word):
                maybe_dict[maybe].append((i, orient))

        # 处理当前字符串在可能字典中的情况
        # 时间复杂度：N^2×C
        ans = set()
        for i, word in enumerate(words):
            if word in maybe_dict:
                for idx, orient in maybe_dict[word]:
                    if i != idx:
                        if orient:
                            ans.add((i, idx))
                        else:
                            ans.add((idx, i))

        return [list(t) for t in ans]


if __name__ == "__main__":
    print(Solution().palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))  # [[0,1],[1,0],[3,2],[2,4]]
    print(Solution().palindromePairs(["bat", "tab", "cat"]))  # [[0,1],[1,0]]
    print(Solution().palindromePairs(["a", "abc", "aba", ""]))  # [[2, 3], [3, 2], [0, 3], [3, 0]]
    print(Solution().palindromePairs(["a", "b", "c", "ab", "ac", "aa"]))  # [[3,0],[1,3],[4,0],[2,4],[5,0],[0,5]]
