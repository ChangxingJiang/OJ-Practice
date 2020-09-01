from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        # 生成反向字符串字典
        reversed_words = {}
        for i, word in enumerate(words):
            reversed_words[word[::-1]] = i

        ans = []

        # 将当前可能添加到可能字典
        for i, word in enumerate(words):
            # 处理字符串为空串的情况
            # 时间复杂度：O(N)*1=O(N)
            if not word:
                for j, another_word in enumerate(words):  # 遍历寻找所有回文字符串
                    if another_word and another_word == another_word[::-1]:
                        ans.append([i, j])
                        ans.append([j, i])

            # 处理字符串为其他字符串的反转的情况
            # 时间复杂度：O(1)*N=O(N)
            if word in reversed_words:
                j = reversed_words[word]
                if i != j:
                    ans.append([i, j])

            # 处理其他情况
            # 时间复杂度(最坏情况)：O(C^2)*N=O(N*C^2)
            for j in range(1, len(word)):  # 遍历字符串中的所有位置
                prefix = word[:j]  # 生成前缀
                suffix = word[-j:]  # 生成后缀
                if prefix in reversed_words and word[j:] == word[j:][::-1]:  # 判断前缀后的部分是否为回文串
                    ans.append([i, reversed_words[prefix]])
                if suffix in reversed_words and word[:-j] == word[:-j][::-1]:  # 判断后缀前的部分是否为回文串
                    ans.append([reversed_words[suffix], i])

        return ans


if __name__ == "__main__":
    print(Solution().palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))  # [[0,1],[1,0],[3,2],[2,4]]
    print(Solution().palindromePairs(["bat", "tab", "cat"]))  # [[0,1],[1,0]]
    print(Solution().palindromePairs(["a", "abc", "aba", ""]))  # [[2, 3], [3, 2], [0, 3], [3, 0]]
    print(Solution().palindromePairs(["a", "b", "c", "ab", "ac", "aa"]))  # [[3,0],[1,3],[4,0],[2,4],[5,0],[0,5]]
