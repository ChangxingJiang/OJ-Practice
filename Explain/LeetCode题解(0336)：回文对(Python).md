# LeetCode题解(0336)：寻找列表中可以通过连接构成回文串的字符串对(Python)

题目：[原题链接](https://leetcode-cn.com/problems/palindrome-pairs/)（困难）

标签：字符串、哈希表、字典树

相关题目：如果使用前后缀分别匹配的方法，可参考题目0214（最短回文串）

| 解法           | 时间复杂度                         | 空间复杂度                       | 执行用时       |
| -------------- | ---------------------------------- | -------------------------------- | -------------- |
| Ans 1 (Python) | $O(N×C^2)$ : 其中C为字符串平均长度 | $O(N×C)$ : 其中C为字符串平均长度 | 932ms (30.05%) |
| Ans 2 (Python) | $O(N×C^2)$ : 其中C为字符串平均长度 | $O(N×C)$ : 其中C为字符串平均长度 | 420ms (99.67%) |
| Ans 3 (Python) |                                    |                                  |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（枚举前缀和后缀）：

```python
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
        for i, word in enumerate(words):
            for maybe, orient in all_palindromes(word):
                maybe_dict[maybe].append((i, orient))

        # 处理当前字符串在可能字典中的情况
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
```

解法二（使用翻转字符串字典用作查询，减少回文串判断）：

![LeetCode题解(0336)：截图1](LeetCode题解(0336)：截图1.png)

```python
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
```

