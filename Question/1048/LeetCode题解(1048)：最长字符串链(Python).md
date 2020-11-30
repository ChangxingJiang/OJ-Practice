# LeetCode题解(1048)：最长字符串链(Python)

题目：[原题链接](https://leetcode-cn.com/problems/longest-string-chain/)（中等）

标签：哈希表、动态规划

| 解法           | 时间复杂度                             | 空间复杂度 | 执行用时       |
| -------------- | -------------------------------------- | ---------- | -------------- |
| Ans 1 (Python) | $O(WlogW+W×L^2logL)$ : 其中L为单词长度 | $O(W)$     | 308ms (31.70%) |
| Ans 2 (Python) |                                        |            |                |
| Ans 3 (Python) |                                        |            |                |

解法一（哈希表）：

```python
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))

        ans = 1
        count = {}
        for word in words:
            size = len(word)
            if size == 1:
                count[word] = 1
            else:
                min_from = float("inf")
                for i in range(size):
                    sorted_word = "".join(sorted(word[:i] + word[i + 1:]))
                    if sorted_word in count:
                        min_from = min(min_from, count[sorted_word])

                if min_from != float("inf"):
                    ans = max(ans, size - min_from + 1)
                    count["".join(sorted(word))] = min_from
                else:
                    count["".join(sorted(word))] = size

        return ans
```